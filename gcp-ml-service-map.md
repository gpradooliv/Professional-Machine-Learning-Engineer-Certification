# Mapa de serviços GCP para ML Engineering

| Problema | Serviço principal | Alternativas | Pergunta de decisão |
|---|---|---|---|
| Armazenar dados brutos | Cloud Storage | BigQuery | Arquivos ou tabelas analíticas? |
| Consultar dados analíticos | BigQuery | Cloud SQL | Workload analítico ou transacional? |
| Treinar ML via SQL | BigQuery ML | Vertex AI Training | O problema cabe em low-code? |
| Treinar modelo customizado | Vertex AI Training | Workbench, GKE | Preciso controlar framework e hardware? |
| Servir API containerizada | Cloud Run | Vertex AI Endpoint, GKE | Serverless simples ou serving especializado? |
| Orquestrar pipeline | Vertex AI Pipelines | Composer | Workflow ML-native ou integração ampla? |
| Criar builds | Cloud Build | GitHub Actions | Onde executar CI/CD? |
| Extrair documentos | Document AI | OCR customizado | Layout e proveniência são críticos? |
| Construir GenAI | Vertex AI / Gemini | Model Garden | Como equilibrar custo, latência e qualidade? |
| Proteger GenAI | Model Armor | Validadores customizados | Quais ataques e vazamentos mitigar? |
