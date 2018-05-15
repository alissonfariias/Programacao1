# coding utf-8

valor_total = float(raw_input('Informe o valor total: '))
data = (raw_input('Informe a data: '))
quantidade_de_produtos = float(raw_input('Informe a quantidade de produtos: '))
media = valor_total / quantidade_de_produtos
print 'Data:', data
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de R$ %.1f.' % (valor_total,media)
