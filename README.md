# Plano de Aula Django Web App

Este é um projeto Django que permite que professores criem e gerenciem planos de aula.

## Funcionalidades

- Cadastro, edição e exclusão de planos de aula.
- Visualização dos detalhes de um plano de aula.
- Geração de PDF estilizado a partir dos detalhes de um plano de aula.

## Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/plano-de-aula-django.git
cd plano-de-aula-django

Crie e ative um ambiente virtual (recomendado):
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

Execute as migrações do banco de dados:
python manage.py migrate

Inicie o servidor de desenvolvimento:
python manage.py runserver

Acesse o aplicativo em http://127.0.0.1:8000/ e comece a usar!

Uso
Crie uma conta de professor ou faça login se já tiver uma.
Acesse a página "Meus Planos de Aula" para visualizar, criar ou editar planos de aula.
Na página de detalhes de um plano de aula, você pode gerar um PDF estilizado clicando no botão "Gerar PDF".

Contribuição
Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

Crie um fork deste repositório.
Crie uma branch para sua nova funcionalidade ou correção de bug: git checkout -b feature-nova-funcionalidade.
Faça as alterações necessárias e adicione novos commits.
Envie um pull request para o repositório original.
Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
Criado por José Eduardo França dos Santos
