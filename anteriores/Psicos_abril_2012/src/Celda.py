#!/usr/bin/env python

"""Clase Celda para el programa psicos"""
class Celda:

    """La celda es el automata de dos estados donde se mueven los agentes.
    La descripcion de los elementos de la celda es el siguiente:

    Blindaje: este elemento sirve en particular en el metodo pelear; el blindaje le ayudara al agente
    a protegerse y asi aumentar sus probabilidades de sobrevivir al ataque del enemigo.

    Camuflaje: este elemento se utiliza para evitar ser visto por el enemigo, es decir, el camuflaje le
    ayudara a un agente a evitar estar en la vision (vease la clase Agente) del enemigo.

    Movilidad: este elemento es utilizado como catalizador al momento de que el agente se mueva, es decir,
    dependiendo del valor facilitarara o dificultara el movimiento del agente.

    Occ: indica si la celda esta ocupada o no por un agente."""
           
    #NO SE PARA QUE SIRVA EL TERRENO, BIEN PODEMOS QUEDARNOS SOLO CON LA MOVILIDAD:
    
    def __init__(self,x,y,blindaje,camuflaje,movilidad,terreno):
        self.x = x
        self.y = y
        self.blindaje=blindaje
        self.camuflaje=camuflaje
        self.movilidad=movilidad
        self.terreno=terreno
        self.occ="False"
        #############ACB-13-02-13#########################
        self.costo=blindaje+camuflaje+movilidad
        self.gscore=0
        self.hscore=0
        self.fscore=0
        self.vecinos=[]
        #######################################
        """Metodo para devolver la ubicacion (en coordenadas de la forma (x,y)) de la celda."""
        def getX(self):
            return self.x

        def getY(self):
            return self.y

	def getBlindaje(self):
		return self.blindaje

	def getCamuflaje(self):
		return self.camuflaje

	def getMovilidad(self):
		return self.movilidad

	def getTerreno(self):
		return self.terreno

    """Metodo que deja una celda ocupada o desocupada de acuerdo al valor que se le pasa como parametro."""
    def setEstado(self,valor):
        self.occ=valor

        """Metodo para obtener el estado de la ocupacion de la celda."""
    def getEstado(self):
        return self.occ

        """Metodo que devuelve una cadena con las caracteristicas de la celda."""
    def __str__(self):
        cadena = "Coords.: " +"("+ str(self.getX()) + "," + str(self.getY()) + ")" + "; ocupado: " + str(self.occ)  + "; blindaje: " + str(self.blindaje) + "; camuflaje: " + str(self.camuflaje) + "; movilidad: " + str(self.movilidad) + "; terreno: "+ str(self.terreno) + ".\n"
        return cadena

    ##########ACB-13-2-13############################

    def set_gscore(self,valor):
        self.gscore=valor

    def get_gscore(self):
        return self.gscore

    def set_hscore(self,valor):
        self.hscore=valor 

    def get_hscore(self):
        return self.hscore

    def set_fscore(self,valor):
        self.fscore=valor 

    def get_fscore(self):
        return self.fscore

    #############################################################



	
