from this import i

nombres_list= ['cerveza importada ','Cerveza nacional','Botella de Vino','Agua',
              'Lechuga','Cebollas','Patatas','Tomates','Naranjas','Plátanos','Manzanas','Ternera','Pechugas de pollo',
              'Queso fresco','docena de huevos','Arroz ','pan','Leche','Coca-Cola / Pepsi botella','Café Cappuccino',
              'Menú de McDonalds, Burger King o similar','Comida para dos en restaurante a la carta','Comida en un restaurante barato',
              'zapatos de hombre de cuero','zapatillas deportivas de marca (Nike, Adidas, Puma, etc.)','vestido (Zara, H&M, etc.)',
              'vaqueros Levis 501 (o equivalente)','Volkswagen Golf ','Gasolina','tarifa taxi','Pase mensual de transporte público','billete de ida en transporte público',
              'Internet (50 Mbps o más, tarifa plana, Cable / ADSL)','Tarifa de prepago móvil ','vivienda en las afueras de la ciudad ',
              'vivienda en el centro de la ciudad ','Vivienda (3 habitaciones) en las afueras','Vivienda (3 habitaciones) en centro de la ciudad',
              'Apartamento (1 dormitorio) en las afueras','Apartamento (1 dormitorio) en el centro de la ciudad','Hipoteca: tasa de interés anual (%)',
              'Salario (sueldo mensual) medio después de impuestos (neto)','Cine','Paquete de cigarrillos (Marlboro)',
              ]


unidades_list= ['litros','boleto','unidad','hora','mes','tiket','latas','paquete','kg','minuto','metro','centimetro','lata','docena','par']


datarec='Cerveza nacional (0,5 litros)'

def ac(name):
    name = name.replace('á', 'a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)


def buscar_nom(datarec):
    for nombre in nombres_list:
        if ac(datarec.lower()).count(ac(nombre.lower())) > 0:
            return nombre


print (buscar_nom(datarec))

def buscar_uni(datarec):
    for uni in unidades_list:
        if ac(datarec.lower()).count(ac(uni.lower())) > 0:
            return uni


print(buscar_uni(datarec))



def buscar_num(datarec):
    cant= len()
    for i in range(0,cant):
        if str(datarec[i].isdigit()) == 'True':
            inicio = i
            #guardr en lista y componer el numero






#print(buscar_num(i))




#funcion para mostrar imagenes segun subcategoria





#funcion para utilizar imagenes predeterminadas


nombrescr= 'precio en supermercados'

def imagen(nombrescr):
    if nombrescr == 'articulos para el hogar':
        nombrescr = "articulos_para_el_hogar"

    elif nombrescr == 'costo educacion':
        nombrescr = 'costo_educacion'

    elif nombrescr == 'gastos de vivienda':
        nombrescr = 'gasto_y_vivienda'

    elif nombrescr == 'infraestructura salud':
        nombrescr = 'infraestructura'

    elif nombrescr == 'infraestructura educacion':
        nombrescr = 'infraestructura_educacion'

    elif nombrescr == 'insumos':
        nombrescr = 'insumo'

    elif nombrescr == 'medicamento':
        nombrescr = 'medicamento'

    elif nombrescr == 'medios de transporte':
        nombrescr = 'medio_transporte'

    elif nombrescr == 'ocio y deportes':
        nombrescr = 'ocio_y_deporte'

    elif nombrescr == 'precio restaurant':
        nombrescr = 'precio_restaurant'

    elif nombrescr == 'precio hoteles':
        nombrescr = 'precio_hoteles'

    elif nombrescr == 'recreacion y cultura':
        nombrescr = 'recreacion_y_cultura'

    elif nombrescr == 'ropa y calazado':
        nombrescr = 'ropa_y_calzado'

    elif nombrescr == 'servicios':
        nombrescr = 'servicio'

    elif nombrescr == 'transprte y servicio':
        nombrescr = 'transporte_y_servicio'

    elif nombrescr == 'vivienda y salario':
        nombrescr = 'vivienda_y_salario'

    elif nombrescr == 'precio en supermercados':
        nombrescr = 'supermercado'


    return (nombrescr+'.png')


#funcion para guardar datos de precio mundi

def palabra(frase):
    # presios supermecados listos
    if frase== 'La cerveza importada (33 latas)':
        return (['cerveza importada','33','latas'])
    elif frase== 'Cerveza nacional (0,5 litros)':
        return (['cerveza nacional','0,5','litros'])
    elif frase== 'Botella de Vino (Calidad media)':
        return (['vino','1', 'botella'])
    elif frase== 'Agua (1,5 litros)':
        return (['agua','1,5','litros'])
    elif frase== 'Lechuga (1 unidad)':
        return (['lechuga','1','unidad'])
    elif frase== 'Cebollas (1kg)':
        return (['cebolla','1', 'kg'])
    elif frase== 'Patatas (1 kg)':
        return (['papas', '1','kg'])
    elif frase== 'Tomates (1 kg)':
        return (['tomates','1','kg'])
    elif frase== 'Naranjas (1 kg)':
        return (['naranjas','1','kg'])
    elif frase== 'Plátanos (1kg)':
        return (['platanos','1','kg'])
    elif frase== 'Manzanas (1 kg)':
        return (['manzanas','1','kg'])
    elif frase== 'Ternera (cadera o similar) (1kg)':
        return (['carne de ternera','1','kg'])
    elif frase=='Pechugas de pollo (1 kg)':
        return (['pechuga de pollo','1','kg'])
    elif frase=='Queso fresco (1 kg)':
        return (['queso fresco', '1', 'kg'])
    elif frase=='Una docena de huevos':
        return (['huevos','1','docena'])
    elif frase== 'Arroz (1kg)':
        return (['arroz','1','kg'])
    elif frase=='Un kilo de pan (1 kg)':
        return (['pan','1','kg'])
    elif frase=='Leche (1 litro)':
        return (['leche','1','kg'])
    # precios restaurante
    elif frase=='Agua (botella de 33 latas)':
        return (['botella de agua','33', 'latas'])
    elif frase=='Coca-Cola / Pepsi (botella de 33latas)':
        return (['coca cola o pepsi','33','latas'])
    elif frase=='Café Cappuccino':
        return (['café cappuccino','1','unidad'])
    elif frase== 'Cerveza importada (botella de 33latas)':
        return (['cervesa importada','33','latas'])
    elif frase=='Cerveza nacional (0,5 litros)':
        return (['cerveza nacional','0,5','litros'])
    elif frase=='Menú de McDonalds, Burger King o similar':
        return (['menú mcdonalds','1','unidad'])
    elif frase== 'Comida para dos en restaurante a la carta (dos platos y postre)':
        return (['menú comida para dos','1','unidad'])
    elif frase=='Comida en un restaurante barato (menú del día)':
        return (['menu del dia','1','unidad'])
    # Precios de ropa y calzado en Chile
    elif frase=='Unos zapatos de hombre de cuero':
        return (['zapaos de hombre','1','par'])
    elif frase=='Unas zapatillas deportivas de marca (Nike, Adidas, Puma, etc.)':
        return (['zapatillas deportivas','1','par'])
    elif frase=='Un vestido (Zara, H&M, etc.)':
        return (['vestido','1','unidad'])
    elif frase=='Unos vaqueros Levis 501 (o equivalente)':
        return (['jeans pantalon','1','unidad'])
    #Precios de transportes y servicios en Chile
    elif frase=='Volkswagen Golf 1.4 90 KW (o un automóvil nuevo equivalente)':
        return (['automovil Volkswagen Golf','1','unidad'])
    elif frase=='Gasolina (1 litro)':
        return (['gasolina','1','litro'])
    elif frase=='Taxi 1 hora de trayecto (tarifa normal)':
        return (['trayecto en taxi','1','hora'])
    elif frase=='Taxi 1km (tarifa normal)':
        return (['trayecto en taxi','1','km'])
    elif frase=='Inicio taxi (tarifa normal)':
        return (['taxi','1','boleto'])
    elif frase=='Pase mensual de transporte público':
        return (['valor mensual transporte publico','1','boleto'])
    elif frase=='Un billete de ida en transporte público':
        return (['transporte publico','1','boleto'])
    elif frase=='Internet (50 Mbps o más, tarifa plana, Cable / ADSL)':
        return (['internet 50mbps','1','mes'])
    elif frase=='1 min. de la Tarifa de prepago móvil local (no hay descuentos o planes)':
        return (['tarifa movil prepago','1','minuto'])
    elif frase=='Básicos (electricidad, gas, agua, basura)':
        return (['gastos basicos (electricidad, gas, agua, basura)','1','mes'])
    #Precios de vivienda y salarios en Chile
    elif frase=='Comprar vivienda en las afueras de la ciudad (precio por m2)':
        return (['precio vivienda zona rural','1','unidad'])
    elif frase=='Comprar vivienda en el centro de la ciudad (precio por m2)':
        return (['precio vivienda zona urbana','1','unidad'])
    elif frase=='Vivienda (3 habitaciones) en las afueras':
        return (['Vivienda (3 habitaciones) zona rural','1','unidad'])
    elif frase=='Vivienda (3 habitaciones) en centro de la ciudad':
        return (['Vivienda (3 habitaciones) zona urbana','1', 'unidad'])
    elif frase=='Apartamento (1 dormitorio) en las afueras':
        return (['apartamento de 1 dormitorio zona rural','1','unidad'])
    elif frase=='Apartamento (1 dormitorio) en el centro de la ciudad':
        return (['Apartamento (1 dormitorio) zora urbana','1','unidad'])
    elif frase=='Hipoteca: tasa de interés anual (%)':
        return (['Hipoteca: tasa de interés anual (%)','1','unidad'])
    elif frase=='Salario (sueldo mensual) medio después de impuestos (neto)':
        return (['sueldo promedio','1','mes'])
    #Precios relacionados con ocio y deporte en Chile
    elif frase=='Paquete de cigarrillos (Marlboro)':
        return (['paquete cigarrillos marlboro','1','unidad'])
    elif frase=='Cine (una entrada / ticket)':
        return (['entrada al cine','1','unidad'])
    elif frase=='Gimnasio (precio por mes)':
        return (['valor gimnasio','1','mes'])
    elif frase=='Alquiler de pista de tenis (1 hora)':
        return (['Alquiler de pista de tenis ','1','hora'])

    return 0
























