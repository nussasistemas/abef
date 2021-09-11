import numpy
import random


def randNumbers(elements, nmin, nmax):
    res = []

    for j in range(elements):
        res.append(random.uniform(nmin, nmax))

    return res


def randomPopulation(i, j, nmin, nmax):
    res = []

    for k in range(i):
        res.append(randNumbers(j, nmin, nmax))
    return res


def calcularFaval(population):
    fx = []
    i = 0

    while i < len(population):
        faval = (baskara(population[i][0]))
        fx.append(abs(faval))
        i = i + 1

    return fx


def ordena(population, fx):
    pop_fx = numpy.c_[population, fx]
    cols = len(pop_fx[0]) - 1
    pop_fx = pop_fx[numpy.argsort(pop_fx[:, cols])]
    return pop_fx[::-1]


def tournament(population, k):
    best = -1
    i = 0

    while i < k:
        ind = random.randint(0, len(population) - 1)

        if (best == -1) or population[ind][len(population[0]) - 1] < population[best][len(population[0]) - 1]:
            best = ind
        i = i + 1
    return best


def selection(population, k):  # População com e quantidade de envolvidos por torneio
    res = numpy.zeros((len(population), len(population[0])))
    i = 0

    while i < len(population):
        ind = tournament(population, k)
        res[i] = population[ind]
        i = i + 1
    cols = len(res[0]) - 1
    res = res[numpy.argsort(res[:, cols])]
    res = numpy.delete(res, cols, 1)
    return res


def crossover(population, cross_rate):
    res = numpy.zeros((len(population), len(population[0])))
    i = 0

    while i < len(population):
        alpha = random.random()

        if alpha > cross_rate:
            res[i] = population[i]
        else:
            j = 0
            while j < len(population[0]):
                beta = random.randint(0, 1)

                if beta == 1 or len(population) <= i + 1:
                    res[i][j] = population[i][j]
                else:
                    res[i][j] = population[i + 1][j]
                j = j + 1
        i = i + 1
    return res


def mutation(population, ger_cont, ger_max, mut_rate, error_rate, lim_inf, lim_sup):
    res = numpy.zeros((len(population), len(population[0])))
    i = 0

    while i < len(population):
        j = 0

        while j < len(population[0]):
            beta = random.random()

            delta = (lim_sup - (ger_cont * lim_inf) / ger_max) * random.random()  # y * pow(random.random(),

            if beta <= mut_rate:
                beta2 = random.randint(0, 1)
                if beta2 == 0:
                    res[i][j] = population[i][j] * (1 - delta)
                else:
                    res[i][j] = population[i][j] * (1 + delta)
            else:
                res[i][j] = population[i][j]
            j = j + 1
        i = i + 1
    return res


def ga(individuals, genes, ger, max_number, f_aval, get_sentence):
    results = []
    # Parâmetros iniciais -----------------------------------------------------
    m = individuals  # Número de indivíduos na população
    n = genes  # Número de genes no cromossomodo
    ger_max = ger  # Número máximo de gerações
    Ain = 0  # Assíntota inferior do espaço de busca
    Asu = max_number  # Assíntota superior do espaço de busca

    lim_inf = 0.5  # Valor estocastico inferior dentro da funcao de mutacao
    lim_sup = 1  # Valor estocastico superior dentro da funcao de mutacao

    tc = numpy.linspace(0.9, 0.2, ger_max)  # Taxa de Cruzamento
    tm = numpy.linspace(0.05, 0.4, ger_max)  # Taxa de Mutação
    tau = 4  # Quantidade de indivíduos escolhidos para torneio
    error_rate = 1e-2  # Taxa de erro para parar o algoritmo

    # Cria a populacao inicial ------------------------------------------------
    Pin = randomPopulation(m, n, Ain, Asu)

    # Carrega algumas variaveis do AG
    melhor_i = numpy.ones(genes + 1) * 10000  # Melhor indivíduo
    fx = []  # Vetor de função de avaliação
    ger = []  # Vetor de gerações
    ger_cont = 0  # Contador de geração

    # x = [[1,2],[3,5],[0,-5]]
    while melhor_i[-1] >= error_rate and ger_cont < ger_max:
        fx = f_aval(Pin)
        pop_fx = ordena(Pin, fx)
        melhor_i = pop_fx[-1]
        pop_sel = selection(pop_fx, tau)
        pop_cross = crossover(pop_sel, tc[ger_cont])
        pop_mut = mutation(pop_cross, ger_cont, ger_max, tm[ger_cont], error_rate, lim_inf, lim_sup)
        Pin = numpy.vstack([pop_mut, melhor_i[:-1]])
        print("[%d] S: %s [%s]" % (ger_cont, get_sentence(melhor_i), melhor_i[-1]))
        ger_cont = ger_cont + 1
        results.append([ger_cont, melhor_i[-1]])

    return results
