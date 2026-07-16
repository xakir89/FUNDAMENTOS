# Elaborar un algoritmo para calcular cada una de las siguientes áreas:
#  • Triangulo
#  • Rombo
#  • Trapecio 

def variable(v):
    while True:  
        x = float(input(f"Ingrese el valor para {v}: "))
        print()
        if x > 0:
            return x
            break
        else:
            print("las medidas deben ser mayores de 0")
    
def area_triangulo():
    base = variable(f"""
                    
          *
         * *
        *   *            
       *     *          
      *********              
      |- base -|  
                               
base del triangulo""")
    altura = variable(f"""
                      
     ---------  *
     |         * *            
   altura     *   *
     |       *     *          
     ------ *********     
                               
    altura del triangulo""")
    area = (base*altura)/2
    return area, base, altura
def area_rombo():
    diagional_mayor = variable(f"""
                               
     ------------------ *
     |                 * *
     |                *   *
     |               *     *
     |              *       *
    Diagonal Mayor *         *
     |              *       *
     |               *     *
     |                *   *
     |                 * *
     ------------------ *   
                                                                                     
diagonal mayor del rombo""")
    diagonal_menor = variable(f"""
                              
                        *
                       * *
                      *   *
                     *     *
                    *       *
                   *         *
                  | *       * |
                  |  *     *  |
                  |   *   *   |
                  |    * *    |
                  |     *     |
                  - Dia Menor - 
                                    
diagonal menor del rombo""")
    area = (diagional_mayor*diagonal_menor)/2
    return area, diagional_mayor, diagonal_menor
def area_trapesio():
    base_mayor = variable(f"""

                **********
               *          *          
              *            *         
             *              *
            ******************                   
            |-- Base Mayor ---| 

                                                  
base mayor del trapesio""")
    base_menor = variable(f"""
                          
               |-Ba Menor-|          
                **********
               *          *          
              *            *         
             *              *
            ******************

base menor del trapesio""")
    altura = variable(f"""
                      
      --------- **********
      |        *          *          
    Altura    *            *         
      |      *              *
      ----- ******************                  

altura del trapesio""")
    if base_mayor > base_menor:
        area = ((base_mayor+base_menor)*altura)/2
    else:
        print("la base mayor debe ser mas grande")
    return area, altura, base_mayor, base_menor

def menu():
    while True:
        print("""
************ BIENVENIDO AL ALGORITMO DE AREAS ************
*                                                        *
*                1. hallar Area Triangulo                *
*                2. hallar Area Rombo                    *
*                3. hallar Area Trapesio                 *
*                4. Salir                                *    
*                                                        *
**********************************************************
        """)
        opc = int(input("Seleccione una Opcion: "))
        if opc == 1:
            area, b, a = area_triangulo()
            print(f"""
******************* AREA DEL TRIANGULO ************************
*                                                             *
*     ---------  *                                            *
*     |         * *            {b:.1f} X {a:.1f}                    *
*   altura     *   *           -----------  = {area:.1f}            *
*     |       *     *                2                        *
*     ------ *********                                        *
*            |- base -|                                       *              
*                                                             *
***************************************************************
        """)            
        elif opc == 2:
            area, dma, dme= area_rombo()
            print(f"""
*************************** AREA DEL ROMBO ***************************
*  ------------------ *                                              *
*  |                 * *                                             *
*  |                *   *               {dma}  X {dme}                *
*  |               *     *     ---------------------------------     *
*  |              *       *                  2                       *
* Diagonal Mayor *         *                                         *
*  |            | *       * |             = {area:.2f}                  *
*  |            |  *     *  |                                        *
*  |            |   *   *   |                                        *
*  |            |    * *    |                                        *
*  -------------|---- *     |                                        *
*               - Dia Menor -                                        *
*                                                                    *
**********************************************************************
        """)   
        elif opc == 3:
            area, a, bmayor, bmenor= area_trapesio()
            print(f"""
******************** AREA DEL TRAPESIO *******************
*                                                        *
*             |-Ba Menor-|                               *
*    --------- **********                                *
*    |        *          *                               *
*  Altura    *            *                              *       
*    |      *              *                             *
*    ----- ******************                            *
*          |-- Base Mayor ---|                           * 
*                                                        *
*     ({bmayor:.1f} + {bmenor:.1f}) X {a}                               *
*   ------------------------       = {area:.2f}              *
*               2                                        *
*                                                        *
**********************************************************
        """)   
        elif opc == 4:
            print("Gracias por confiar en nosotros")
            print()
            break
        else:
            print("Dato errado la opcion solo puede ser 1 al 4")
menu()



