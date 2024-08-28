import clips

env = clips.Environment()

env.build('(deftemplate cliente (slot preferencias) (slot tipo_viaje) (slot presupuesto))')
env.build('(deftemplate recomendacion (slot destino))')

env.build('''
(defrule aventura-bajo-presupuesto-grupal
    (cliente (preferencias aventura) (tipo_viaje grupal) (presupuesto bajo))
    =>
    (assert (recomendacion (destino "Excursión a las montañas"))))
''')

env.build('''
(defrule aventura-medio-presupuesto-grupal
    (cliente (preferencias aventura) (tipo_viaje grupal) (presupuesto medio))
    =>
    (assert (recomendacion (destino "Cueva La Vaca"))))
''')

env.build('''
(defrule aventura-alto-presupuesto-grupal
    (cliente (preferencias aventura) (tipo_viaje grupal) (presupuesto alto))
    =>
    (assert (recomendacion (destino "Viaje a Groenlandia"))))
''')

env.build('''
(defrule aventura-alto-presupuesto-individual
    (cliente (preferencias aventura) (tipo_viaje individual) (presupuesto alto))
    =>
    (assert (recomendacion (destino "Viaje a egipto"))))
''')

env.build('''
(defrule aventura-medio-presupuesto-individual
    (cliente (preferencias aventura) (tipo_viaje individual) (presupuesto medio))
    =>
    (assert (recomendacion (destino "Safari en África"))))
''')

env.build('''
(defrule aventura-bajo-presupuesto-individual
    (cliente (preferencias aventura) (tipo_viaje individual) (presupuesto bajo))
    =>
    (assert (recomendacion (destino "Lanzarse de paracaídas"))))
''')

env.build('''
(defrule aventura-alto-presupuesto-familiar
    (cliente (preferencias aventura) (tipo_viaje familiar) (presupuesto alto))
    =>
    (assert (recomendacion (destino "Disney World"))))
''')

env.build('''
(defrule aventura-medio-presupuesto-familiar
    (cliente (preferencias aventura) (tipo_viaje familiar) (presupuesto medio))
    =>
    (assert (recomendacion (destino "Desierto de la Tatacoa"))))
''')

env.build('''
(defrule aventura-bajo-presupuesto-familiar
    (cliente (preferencias aventura) (tipo_viaje familiar) (presupuesto bajo))
    =>
    (assert (recomendacion (destino "Comfama Arvi"))))
''')

env.build('''
(defrule playa-alto-presupuesto-familiar
    (cliente (preferencias playa) (tipo_viaje familiar) (presupuesto alto))
    =>
    (assert (recomendacion (destino "Resort de lujo en el Caribe"))))
''')

env.build('''
(defrule playa-medio-presupuesto-familiar
    (cliente (preferencias playa) (tipo_viaje familiar) (presupuesto medio))
    =>
    (assert (recomendacion (destino "Decameron Cartegena"))))
''')

env.build('''
(defrule playa-bajo-presupuesto-familiar
    (cliente (preferencias playa) (tipo_viaje familiar) (presupuesto bajo))
    =>
    (assert (recomendacion (destino "Hotel a dos cuadras de la playa"))))
''')

env.build('''
(defrule ciudad-medio-presupuesto
    (cliente (preferencias ciudad) (tipo_viaje individual) (presupuesto medio))
    =>
    (assert (recomendacion (destino "Tour cultural en París"))))
''')


env.build('''
(defrule naturaleza-bajo-presupuesto
    (cliente (preferencias naturaleza) (tipo_viaje familiar) (presupuesto bajo))
    =>
    (assert (recomendacion (destino "Camping en un parque nacional"))))
''')

env.build('''
(defrule cultura-medio-presupuesto
    (cliente (preferencias cultura) (tipo_viaje grupal) (presupuesto medio))
    =>
    (assert (recomendacion (destino "Visita a los templos de Japón"))))
''')

def generar_recomendacion(preferencias=None, tipo_viaje=None, presupuesto=None):
    env.reset()

    if preferencias and tipo_viaje and presupuesto:
        env.assert_string(f'(cliente (preferencias {preferencias}) (tipo_viaje {tipo_viaje}) (presupuesto {presupuesto}))')

    env.run()

    recomendaciones = []
    for fact in env.facts():
        if fact.template.name == 'recomendacion':
            recomendaciones.append(fact['destino'])

    return recomendaciones