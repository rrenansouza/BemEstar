# Bem Estar - Casa de Repouso e Longa Permanência

## Overview
Landing page responsiva e profissional para casa de repouso / residência de longa permanência para idosos. Design clean e minimalista com paleta de cores em tons suaves de azul e verde, transmitindo calma, acolhimento e segurança.

## Current State
- Landing page completa e funcional
- Design responsivo mobile-first
- Sistema de contato e candidaturas com banco de dados
- Painel administrativo com login/senha

## Project Structure
```
/
├── index.html              # Página principal com HTML, CSS e JS
├── app.py                  # Servidor Flask com rotas API e admin
├── templates/
│   ├── admin_login.html    # Tela de login do admin
│   └── admin_dashboard.html # Painel administrativo
├── static/
│   ├── logo.png            # Logo da Bem Estar
│   ├── hero-image.png      # Imagem da Hero Section
│   ├── daycare-image.png   # Imagem da seção Daycare
│   └── gallery-[1-15].png  # 15 imagens da galeria Nossa Estrutura
├── uploads/                # Currículos enviados
└── replit.md               # Documentação do projeto
```

## Features Implemented
1. **Hero Section** - Título com fonte Poppins, imagem personalizada, botões "Saiba Mais" e "Entrar em contato"
2. **Quem Somos** - Missão, valores e proposta de cuidado humanizado
3. **Serviços** - 9 cards (Enfermagem 24h, Consultas, Fisioterapia, Psicologia, Nutrição, Atividades, Musicoterapia, Eventos Comemorativos, Oficinas)
4. **Galeria** - Grid de 15 imagens reais da casa + link para fotos do Facebook
5. **Números** - Estatísticas de credibilidade com animação de contagem ao scroll
6. **Depoimentos** - 3 cards de depoimentos de familiares
7. **Daycare** - Serviço complementar de cuidados diurnos com imagem personalizada
8. **Trabalhe Conosco** - Formulário limpo com toggle iOS para aceitar freelances
9. **Contato** - Formulário completo + informações de contato + mapa
10. **WhatsApp Flutuante** - Botão fixo no canto inferior direito
11. **Footer** - Redes sociais (Facebook e Instagram) sem logo
12. **Admin Panel** - Painel para visualizar contatos e candidaturas

## Technical Details
- **Frontend**: HTML5, CSS3 (Flexbox/Grid), JavaScript vanilla
- **Backend**: Python Flask com SQLAlchemy
- **Database**: PostgreSQL (Neon-backed)
- **Tipografia**: Google Fonts (Poppins)
- **Paleta de Cores**:
  - Azul principal: #5B9BD5
  - Azul claro: #E8F4FC
  - Verde apoio: #7BC9A6
  - Verde claro: #E8F8F0

## Admin Panel
- **URL**: /admin
- **Usuário**: admin
- **Senha**: bemestar2024
- Visualizar contatos recebidos
- Visualizar candidaturas de emprego
- Download de currículos
- Marcar como lido / Excluir

## Contact Information
- **Telefone/WhatsApp**: (11) 96160-1799
- **E-mail**: bemestarestadia@gmail.com
- **Endereço**: Rua Professor Benedito Alarico de Castro Borelli, 214 - Parque São Domingos, São Paulo - SP, CEP 05122-000

## Social Media
- **Facebook**: https://www.facebook.com/bemestarestadia
- **Instagram**: https://www.instagram.com/bemestarestadia/

## API Endpoints
- `POST /api/contato` - Recebe formulário de contato
- `POST /api/trabalhe-conosco` - Recebe candidatura de emprego

## Recent Changes
- 2024-12-04: Landing page inicial criada
- 2024-12-04: Alterado de "Vida Plena" para "Bem Estar"
- 2024-12-04: Adicionado logo da empresa
- 2024-12-04: Atualizado WhatsApp para (11) 96160-1799
- 2024-12-04: Adicionados serviços de Musicoterapia e Eventos Comemorativos
- 2024-12-04: Adicionado link para fotos do Facebook
- 2024-12-04: Criada seção "Trabalhe Conosco" com formulário
- 2024-12-04: Atualizado endereço e informações de contato
- 2024-12-04: Adicionado mapa com links Google Maps/Waze
- 2024-12-04: Adicionados ícones de redes sociais no footer
- 2024-12-04: Criado painel administrativo com banco de dados
- 2024-12-04: Removido "Contato" do header
- 2024-12-04: Atualizada imagem da Hero Section com imagem personalizada
- 2024-12-04: Removidos ícones de benefícios da Hero Section
- 2024-12-04: Adicionada animação de contagem aos números em "Nossa Trajetória"
- 2024-12-04: Atualizada imagem da seção Daycare
- 2024-12-04: Removida lista de vagas do "Trabalhe Conosco"
- 2024-12-04: Adicionado toggle iOS para aceitar freelances no formulário de candidatura
- 2024-12-04: Restaurados botões "Saiba Mais" e "Entrar em contato" na Hero Section
- 2024-12-04: Removido logo do Footer
- 2024-12-04: Adicionadas 15 imagens reais na seção "Nossa Estrutura"
