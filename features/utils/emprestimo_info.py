class GerarInfoEmprestimo:

    @staticmethod
    def gerar_cpf():
        from pycpfcnpj import gen

        return gen.cpf()

    @staticmethod
    def gerar_nome():
        from random import choice

        nome = ['Felipe', 'Anderson', 'Mercedes', 'Camila', 'Mariano', 'Gabrielly', 'Monique']
        return nome[choice(range(len(nome)))]

    @staticmethod
    def info_emprestimo():
        import random
        from random import choice

        parcelas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        vl_emprestimo = random.randint(10, 10000)
        nr_parcelas = parcelas[choice(range(len(parcelas)))]

        vl_parcelas = vl_emprestimo / nr_parcelas

        cpf = GerarInfoEmprestimo.gerar_cpf()
        nome = GerarInfoEmprestimo.gerar_nome()

        number_id = random.randint(10, 1000)

        info_emp = {
           'id': number_id,
           'nome': nome,
           'cpf': cpf,
           'vl_emprestimo': vl_emprestimo,
           'nr_parcelas': nr_parcelas,
           'vl_parcelas': vl_parcelas
        }

        return info_emp
