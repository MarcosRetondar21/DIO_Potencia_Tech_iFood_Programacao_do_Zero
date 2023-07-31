# Aplicativo Bancário Simples

Este é um aplicativo bancário simples que permite realizar operações básicas como depósito, saque e verificar o extrato da conta. O código foi escrito em Python e pode ser executado em qualquer ambiente compatível com Python.

## Funcionalidades

### 1. Depositar

Ao selecionar a opção 'Depositar', você poderá informar o valor que deseja depositar na conta. O aplicativo validará se o valor é válido (maior que zero) antes de efetuar o depósito. O valor depositado será somado ao saldo da conta e registrado no extrato.

### 2. Sacar

Se você escolher a opção 'Sacar', poderá inserir o valor que deseja sacar. O aplicativo verificará algumas condições antes de autorizar o saque:

- Se o valor do saque for maior que o saldo disponível na conta, o saque será negado com a mensagem "Opção falhou! Você não tem saldo em conta".
- Se o valor do saque for maior que o limite diário permitido (R$500), o saque será negado com a mensagem "Opção falhou! Você excedeu o limite por saque".
- Se o número máximo de saques diários (3) for atingido, o saque será negado com a mensagem "Opção falhou! Número máximo de saques excedido".
- Se o valor informado for válido (maior que zero) e todas as condições forem atendidas, o valor será subtraído do saldo da conta, o saque será registrado no extrato e o contador de saques será incrementado.

### 3. Extrato

Ao selecionar a opção 'Extrato', o aplicativo exibirá um resumo das operações realizadas na conta. Caso não tenha sido feita nenhuma operação, a mensagem "Não foram realizadas operações" será exibida. Caso contrário, o extrato mostrará os detalhes dos depósitos e saques realizados, bem como o saldo atual da conta.

### 0. Sair

Ao selecionar a opção 'Sair', o aplicativo será encerrado.

## Limitações

Este aplicativo bancário simples foi desenvolvido apenas para fins educacionais e não possui recursos de segurança ou persistência de dados. Ele não é adequado para uso em produção ou em ambientes reais de serviços bancários. Além disso, o código não contempla tratamentos avançados de erros ou validações mais complexas.

## Como Executar

Para executar o aplicativo, copie e cole o código em um ambiente Python compatível (por exemplo, o ambiente Jupyter Notebook, Visual Studio Code com o Python extension, Google Colab ou outro ambiente Python instalado em sua máquina local). Em seguida, execute o código e siga as instruções do menu para interagir com o aplicativo. Lembre-se de que você pode personalizar e estender o código conforme necessário para atender a requisitos adicionais.

**Observação**: Certifique-se de que todas as dependências necessárias estejam instaladas em seu ambiente Python antes de executar o código.
