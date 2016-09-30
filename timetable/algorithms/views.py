from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect

from timetable.algorithms.forms import DantzigForm

from pprint import pprint


def dantzig(request):
    if request.method == 'GET':  # request.GET.:
        form = DantzigForm(request.GET)
        if form.is_valid():
            return HttpResponseRedirect("/dantzig/matrix/?dimension=" + request.GET['dimension'])
    form = DantzigForm()
    return render_to_response("algorithms/dantzig.html", {'form': form}, context_instance=RequestContext(request))


def dantzig_matrix(request):
    if request.method == 'GET' and 'dimension' in request.GET:
        try:
            dimension = int(request.GET['dimension'])
        except ValueError:
            return HttpResponseRedirect("/dantzig/")
        return render_to_response("algorithms/dantzig_matrix.html", {'dimension': range(1, dimension + 1)},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        normalized_matrix, infinity = normalization(request.POST['number_counts'], request.POST)
        res_html_alphabetic = dantzig_algorithm(normalized_matrix)
        res_html_alphabetic = res_html_alphabetic.replace(str(infinity), "&#8734;")
        return render_to_response("algorithms/dantzig_matrix_res.html", {'res_html_alphabetic': res_html_alphabetic},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/dantzig/")


def normalization(count, d=None, infinity=10000):
    count = int(count)
    matrix = [[] for i in range(count)]
    for i in range(1, count + 1):
        for j in range(1, count + 1):
            if d.get('number' + str(i) + str(j)) == "∞":
                matrix[i - 1].append(infinity)
            else:
                matrix[i - 1].append(int(d.get('number' + str(i) + str(j))))
    return matrix, infinity


def dantzig_algorithm(d0, length=5):
    res_matrix = []  # вычисляема матрица
    # way_matrix = []
    d0_length = len(d0)  # размер исходной/вычисляемой матрицы

    res_html_alphabetic = ""

    for i in range(d0_length):  # создание вычисляемой матрицы
        res_matrix.append([])  # квадртаной матрицы, типа [[[], []], [[], []]]
        for j in range(d0_length):
            res_matrix[i].append(0)

    # for i in range(d0_length):  # создание матрицы путей
    #    way_matrix.append([])  # квадртаной матрицы, типа [[[], []], [[], []]]
    #    for j in range(d0_length):
    #        pass
    #        way_matrix[i].append([])

    for i in range(d0_length):
        res_matrix[i][i] = 0

    for m in range(1, d0_length):
        for j in range(0, m):
            res_html_numerical = ""

            if m < length:
                res_html_alphabetic += "<p>d<sup>" + str(m + 1) + "</sup><sub>" + str(m + 1) + ',' + str(
                    j + 1) + "</sub> = min {"
                res_html_alphabetic += "d<sup>0</sup><sub>" + str(m + 1) + ",1</sub> + d<sup>" + str(
                    m) + "</sup><sub>1," + str(
                    j + 1) + "</sub>"

            min_val = d0[m][0] + res_matrix[0][j]

            if m < length:
                res_html_numerical += "min{" + str(d0[m][0]) + " + " + str(res_matrix[0][j])

            for i in range(1, m):

                if m < length:
                    res_html_alphabetic += "; d<sup>0</sup><sub>" + str(m + 1) + "," + str(
                        i + 1) + "</sub> + d<sup>" + str(m) + "</sup><sub>" + str(i + 1) + ',' + str(j + 1) + "</sub>"

                inter = d0[m][i] + res_matrix[i][j]

                if m < length:
                    res_html_numerical += "; " + str(d0[m][i]) + " + " + str(res_matrix[i][j])

                min_val = min(min_val, inter)

            res_matrix[m][j] = min_val

            if m < length:
                res_html_alphabetic += "} = " + res_html_numerical + "} = " + str(min_val) + "<p>"

        for i in range(0, m):

            res_html_numerical = ""

            if m < length:
                res_html_alphabetic += "<p>d<sup>" + str(m + 1) + "</sup><sub>" + str(i + 1) + ',' + str(
                    m + 1) + "</sub> = min {"
                res_html_alphabetic += "d<sup>" + str(m) + "</sup><sub>" + str(
                    i + 1) + ",1</sub> + d<sup>0</sup><sub>1," + str(
                    m + 1) + "</sub>"

            min_val = res_matrix[i][0] + d0[0][m]

            if m < length:
                res_html_numerical += "min{" + str(res_matrix[i][0]) + " + " + str(d0[0][m])

            for j in range(1, m):

                if m < length:
                    res_html_alphabetic += "; d<sup>" + str(m) + "</sup><sub>" + str(i + 1) + "," + str(
                        j + 1) + "</sub> + d<sup>0</sup><sub>" + str(j + 1) + ',' + str(m + 1) + "</sub>"

                inter = res_matrix[i][j] + d0[j][m]

                if m < length:
                    res_html_numerical += "; " + str(res_matrix[i][j]) + " + " + str(d0[j][m])

                min_val = min(min_val, inter)
            res_matrix[i][m] = min_val

            if m < length:
                res_html_alphabetic += "} = " + res_html_numerical + "} = " + str(min_val) + "<p>"

        for i in range(0, m):
            for j in range(0, m):
                if i == j:
                    continue
                res_html_numerical = ""
                if m < length:
                    res_html_alphabetic += "<p>d<sup>" + str(m + 1) + "</sup><sub>" + str(i + 1) + ',' + str(
                        j + 1) + "</sub> = min {"
                    res_html_alphabetic += "d<sup>" + str(m + 1) + "</sup><sub>" + str(i + 1) + "," + str(
                        m + 1) + "</sub> + d<sup>" + str(m + 1) + "</sup><sub>" + str(m + 1) + "," + str(
                        j + 1) + "</sub>, d<sup>" + str(m) + "</sup><sub>" + str(
                        i + 1) + "," + str(j + 1) + "</sub>} = "

                if (res_matrix[i][m] + res_matrix[m][j] < res_matrix[i][j]):
                    # way_matrix[i][j].append(((i, m), (m, j),) )
                    res_matrix[i][j] = res_matrix[i][m] + res_matrix[m][j]
                else:
                    # way_matrix[i][j].append((i, j,) )
                    res_matrix[i][j] = res_matrix[i][j]

                if m < length:
                    res_html_numerical += "min { " + str(res_matrix[i][m]) + " + " + str(res_matrix[m][j]) + ", " + str(
                        res_matrix[i][j]) + "} = " + str(res_matrix[i][j]) + "<p>"
                    res_html_alphabetic += res_html_numerical

        res_html_alphabetic += make_table(res_matrix, m)
    # pprint(way_matrix)
    return res_html_alphabetic


def make_table(matrix, count=0, offset=1):
    if count == 0:
        count = len(matrix)
    else:
        count += 1
    res_html_table = "<p style='margin-left:15px;'>Матрица D" + str(
        count) + '</p><div class="break-matrix"><table frame="border" rules="all" class="matrix-table"><tr><th>'
    for i in range(count):
        res_html_table += "<th>X<sub>" + str(i + offset) + "</sub></th>"
    res_html_table += "</tr>"
    for i in range(count):
        res_html_table += "<tr><td>X<sub>" + str(i + offset) + "</sub></td>"
        for j in range(count):
            res_html_table += "<td>" + str(matrix[i][j]) + "</td>"
        res_html_table += "</tr>"
    res_html_table += "</table></div>"
    return res_html_table
