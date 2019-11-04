# Created by yaveira at 04/11/2019
# language: pt

Funcionalidade: Disponibilizar endpoint para consulta e criação de empréstimo
  Como interface
  Gostaria de consultar e criar empréstimos via endpoint
  Para que possa fazer a interface para o usuário

  @criar_emprestimo @token
  Esquema do Cenário: Criar empréstimo
    Dado que o client possue todos os dados necessários para criação do empréstimo
    Quando envio todos os dados para o serviço de criação de empréstimo
      | endpoint   |
      | <endpoint> |
    Então devo visualizar o status code "200" para criação com sucesso

    Exemplos:
      | endpoint           |
      | api/v1/emprestimos |

  @consultar_emprestimo @token
  Esquema do Cenário: Consultar empréstimo
    Dado que o client tem um empréstimo criado
    Quando o client consultar o serviço de empréstimo informando o ID do empréstimo
      | endpoint   |
      | <endpoint> |
    Então devo visualizar o status code "200"
    E o serviço deve me retornar o status empréstimo "Criado"
    E o serviço deve me retornar o id do empréstimo

    Exemplos:
      | endpoint               |
      | api/v1/emprestimos/{0} |