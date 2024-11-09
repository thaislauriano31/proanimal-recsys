# Sistema de Recomendação de Adoção da ProAnimal

## Visão Geral
Este sistema foi desenvolvido para auxiliar no processo de adoção de animais, oferecendo recomendações personalizadas com base nas preferências do usuário. O sistema utiliza a biblioteca Streamlit para criar uma interface web interativa e intuitiva.

## Estrutura do Código

### 1. Importações e Configuração Inicial
```python
import pandas as pd
import streamlit as st
from recommender import recommender, get_nota_maxima
```
- Pandas: utilizado para manipulação dos dados
- Streamlit: framework para criação da interface web
- Módulo recommender: contém a lógica de recomendação personalizada

### 2. Carregamento de Dados
```python
def load_data():
    df = pd.read_csv('dataset/dogs_data_tratado.csv')
    df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
    df['energia'] = pd.to_numeric(df['energia'], errors='coerce')
    return df
```
- Carrega o dataset dos animais
- Converte as colunas 'idade' e 'energia' para valores numéricos
- Trata possíveis erros de conversão com `errors='coerce'`

### 3. Funções de Navegação
```python
def next_animal():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(st.session_state.filtered_df)

def prev_animal():
    st.session_state.current_index = (st.session_state.current_index - 1) % len(st.session_state.filtered_df)
```
- Gerenciam a navegação entre os animais filtrados
- Utilizam operador módulo (%) para criar uma navegação cíclica
- Mantêm o estado através do `session_state` do Streamlit

### 4. Exibição de Animais
```python
def display_animal():
    if 'filtered_df' in st.session_state:
        # Lógica de exibição do animal atual
```
- Função responsável por exibir as informações do animal atual
- Verifica se existem animais filtrados antes de tentar exibir
- Mostra imagem, descrição e características do animal
- Inclui botões de navegação

### 5. Interface do Usuário

#### Cabeçalho
- Logo do sistema
- Título e subtítulo

#### Formulário de Filtros
O formulário coleta as seguintes informações:
- Idade do animal (faixas etárias)
- Porte (pequeno, médio, grande)
- Status de vacinação
- Status de castração
- Compatibilidade com outros animais
- Necessidades especiais
- Nível de energia

#### Processamento dos Filtros
```python
if submitted:
    filtros_usuario = {
        "idade": idades,
        "porte": porte,
        # ... outros filtros
    }
```
- Quando o formulário é submetido, cria um dicionário com as preferências
- Inicializa o DataFrame filtrado
- Reset do índice de navegação

## Fluxo de Operação

1. **Inicialização**
   - Sistema carrega o dataset
   - Apresenta o formulário de filtros

2. **Submissão do Formulário**
   - Usuário preenche preferências
   - Sistema filtra animais compatíveis
   - Inicializa a exibição do primeiro animal

3. **Navegação**
   - Usuário pode navegar entre animais filtrados
   - Botões "Anterior" e "Próximo"
   - Navegação circular (volta ao início após último animal)

4. **Exibição de Informações**
   - Foto do animal
   - Nome e descrição
   - Características principais
   - Pontuação de compatibilidade

## Gerenciamento de Estado
O sistema utiliza o `session_state` do Streamlit para:
- Manter o DataFrame filtrado entre recarregamentos
- Controlar o índice do animal atual
- Permitir navegação sem perder o contexto

## Notas Importantes
1. O sistema recarrega a página a cada interação (comportamento padrão do Streamlit)
2. As imagens devem estar na pasta `images` com o nome do animal
3. O score de compatibilidade é calculado com base nas preferências do usuário

## Possíveis Melhorias
1. Adicionar cache para otimizar carregamento
2. Implementar filtros adicionais
3. Adicionar sistema de favoritos
4. Melhorar a responsividade da interface
5. Adicionar mais informações sobre cada animal

## Requisitos Técnicos
- Python 3.x
- Streamlit
- Pandas
- Arquivo CSV com dados dos animais
- Pasta de imagens com fotos dos animais
