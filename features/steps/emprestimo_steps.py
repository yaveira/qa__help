from features.pages.emprestimo_page import Emprestimo
from behave import given, when, then
from hamcrest import assert_that, equal_to
from json import loads


@given(u'que o client possue todos os dados necessários para criação do empréstimo')
def step_impl(context):
    from features.utils.emprestimo_info import GerarInfoEmprestimo

    context.dados_emprestimo = GerarInfoEmprestimo.info_emprestimo()


@when(u'envio todos os dados para o serviço de criação de empréstimo')
def step_impl(context):
    endpoint = context.table[0]["endpoint"]

    Emprestimo.criar_emprestimo(context, endpoint)


@then(u'devo visualizar o status code "{code}" para criação com sucesso')
def step_impl(context, code):
    assert_that(int(code), equal_to(context.response.status_code))


@given(u'que o client tem um empréstimo criado')
def step_impl(context):
    context.execute_steps(u"""
        Dado que o client possue todos os dados necessários para criação do empréstimo
        Quando envio todos os dados para o serviço de criação de empréstimo
            | endpoint           |
            | api/v1/emprestimos |
        """)


@when(u'o client consultar o serviço de empréstimo informando o ID do empréstimo')
def step_impl(context):
    endpoint = context.table[0]["endpoint"]

    Emprestimo.consultar_emprestimo(context, endpoint)


@then(u'devo visualizar o status code "{code}"')
def step_impl(context, code):
    assert_that(int(code), equal_to(context.response.status_code))


@then(u'o serviço deve me retornar o status empréstimo "{status_emprestimo}"')
def step_impl(context, status_emprestimo):
    response_status_api = loads(context.response.text)

    assert_that(status_emprestimo, equal_to(response_status_api['status']))


@then(u'o serviço deve me retornar o id do empréstimo')
def step_impl(context):
    id_emprestimo = context.dados_emprestimo['id']
    response_status_api = loads(context.response.text)

    assert_that(response_status_api['id-emprestimo'], equal_to(id_emprestimo))
