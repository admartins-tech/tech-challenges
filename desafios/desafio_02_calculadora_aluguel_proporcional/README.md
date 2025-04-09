# Calculadora de Aluguel Proporcional

Este projeto resolve um problema comum no mercado imobiliário: **calcular automaticamente o valor proporcional do aluguel quando o cliente entra no imóvel no meio do mês**.

A solução foi desenvolvida com foco em:
- Código limpo e modular.
- Boas práticas de engenharia de software.
- Experiência clara e amigável para o usuário final.

---

## Descrição do problema

Quando um cliente aluga um imóvel e entra na metade do mês, ele não deve pagar o valor integral.  
Este projeto automatiza o cálculo do valor proporcional do aluguel, considerando:

-  Valor total do aluguel mensal.
-  Data de entrada do cliente (dia/mês/ano).
-  Quantidade real de dias no mês da entrada (considerando meses com 28, 30 ou 31 dias).

### Exemplo:

- **Valor do aluguel:** R$ 3.000,00
- **Data de entrada:** 15/03/2025
- **Resultado:** R$ 1.645,16 (considerando 17 dias proporcionais)

> A solução proporciona transparência para locadores e locatários, simulando o valor proporcional de maneira prática e precisa.

---

## Tecnologias utilizadas

- **Python 3.x**
- Biblioteca nativa `calendar` para cálculo automático dos dias do mês
- Código estruturado em funções modulares para facilidade de manutenção e leitura

---

## Como executar o projeto

### Pré-requisitos

- Python 3.x instalado na sua máquina.
- Terminal ou prompt de comando configurado.

### Passo a passo:

1. **Clone o repositório principal:**

```bash
git clone https://github.com/admartins-tech/brilliant_youth_21_dias.git
```

2. **Acesse a pasta do repositório clonado:**

```bash
cd brilliant_youth_21_dias
```

3. **Acesse a pasta do desafio específico:**

```bash
cd desafios/desafio_02_calculadora_aluguel_proporcional
```

4. **(Opcional, mas recomendado) Crie um ambiente virtual:**

```bash
python -m venv venv
```

5. **Ative o ambiente virtual:**

- No Windows:

```bash
venv\Scripts\activate
```


- No macOS/Linux:

```bash
source venv/bin/activate
```

6. **Execute o programa:**

```bash
python desafio_02_calculadora_aluguel_proporcional.py
```

7. **Siga as instruções no terminal:**
   - Informe seu nome.
   - Escolha o imóvel alugado.
   - Informe a data de entrada no formato **DD/MM/AAAA**.

8. **Visualize o cálculo do valor proporcional diretamente no terminal.**

Pronto! O programa exibirá para você o valor proporcional de aluguel de forma personalizada.