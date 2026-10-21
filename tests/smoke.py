"""Smoke HTTP integrado. Sólo elimina documentos sintéticos creados por esta ejecución."""
from io import BytesIO
import hashlib
import os
from pathlib import Path
from time import monotonic, sleep
from uuid import uuid4

import httpx
from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject


def pdf(text):
    writer = PdfWriter()
    page = writer.add_blank_page(300, 300)
    font = DictionaryObject({NameObject('/Type'): NameObject('/Font'), NameObject('/Subtype'): NameObject('/Type1'), NameObject('/BaseFont'): NameObject('/Helvetica')})
    page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): font})})
    stream = DecodedStreamObject()
    stream.set_data(f'BT /F1 12 Tf 10 250 Td ({text}) Tj ET'.encode('ascii'))
    page[NameObject('/Contents')] = writer._add_object(stream)
    output = BytesIO()
    writer.write(output)
    return output.getvalue()


def run():
    original = pdf('Original ' + uuid4().hex)
    replacement = pdf('Updated ' + uuid4().hex)
    with httpx.Client(base_url=os.getenv('BASE_URL', 'http://localhost:8080'), timeout=30, trust_env=False) as client:
        deadline = monotonic() + 90
        while monotonic() < deadline:
            try:
                if all(client.get('/health/' + service).status_code == 200 for service in ['ingest', 'extract', 'documents']):
                    break
            except httpx.TransportError:
                pass
            sleep(1)
        else:
            raise RuntimeError('Los servicios no están disponibles')
        assert client.get('/').status_code == 200
        assert client.post('/internal/documents', json={}).status_code == 404
        extracted = client.post('/extract', content=original, headers={'Content-Type': 'application/pdf'})
        assert extracted.status_code == 200, extracted.text
        assert extracted.json()['page_count'] == 1
        assert '## Página 1' in extracted.json()['content']
        assert 'Original ' in extracted.json()['text']
        multipart = client.post('/extract', files={'file': ('a.pdf', original)})
        assert multipart.status_code == 200, multipart.text
        response = client.post('/documents/upload', files={'file': ('demo.pdf', original)})
        assert response.status_code == 201, response.text
        created = response.json()
        doc_id = created['id']
        try:
            assert created['checksum'] == hashlib.sha256(original).hexdigest()
            assert created['text'] == extracted.json()['text']
            assert client.get('/documents/' + doc_id).status_code == 200
            assert any(doc['id'] == doc_id for doc in client.get('/documents/').json())
            assert client.post('/documents/upload', files={'file': ('other.pdf', original)}).status_code == 409
            updated = client.put('/documents/' + doc_id, files={'file': ('new.pdf', replacement)})
            assert updated.status_code == 200, updated.text
            assert updated.json()['created_at'] == created['created_at']
            assert 'Updated ' in updated.json()['text']
            assert client.post('/documents/upload', files={'file': ('bad.pdf', b'bad')}).status_code == 400
            assert client.post('/documents/upload', files={'file': ('large.pdf', b'%PDF-' + b'x' * (5*1024*1024))}).status_code == 413
        finally:
            assert client.delete('/documents/' + doc_id).status_code == 204
        assert client.get('/documents/' + doc_id).status_code == 404
    print('Smoke integrado aprobado: frontend, contrato extract, multipart, CRUD, duplicado, inválido, tamaño y rutas internas.')


if __name__ == '__main__':
    run()
