import pygal
'''
need to import lxml
'''

pieChart = pygal.Pie()
pieChart.add('Amazon', 70)
pieChart.add('ezBuy', 20)
pieChart.add('Lazada', 10)

pieChart.render_in_browser()

