#coding:utf-8
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer
import time


urls = ["https://topcustomhats.com"]
loader = AsyncHtmlLoader(urls)
docs = loader.load()
print(docs)
html2text = Html2TextTransformer()
docs_transformed = html2text.transform_documents(docs)
print(docs_transformed[0].page_content)
