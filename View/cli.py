from models.LinkedList import LinkedList

def main():
    lista = LinkedList()

    while True:

        user_input = (input().upper().split(" "))
        
        if user_input[0] in ["RPI","RPF","RPDE","RPAE", "RPII" ,"VNE" , "VP" , "EPE" ,"EUE" ,"EP"]:

            if user_input[0]=="RPI" and len(user_input)==2:
                lista.insert_at_start(user_input[1])
                lista.traverse_list()

            elif user_input[0]=="RPF" and len(user_input)==2:
                lista.insert_at_end(user_input[1])
                lista.traverse_list()
            
            elif user_input[0]=="RPDE" and len(user_input)==3:
                lista.insert_after_item(user_input[1] , user_input[2])
                lista.traverse_list()
            
            elif user_input[0]=="RPAE" and len(user_input)==3:
                lista.insert_before_item(user_input[2],user_input[1])
                lista.traverse_list()
            
            elif user_input[0]=="RPII" and len(user_input)==3:
                lista.insert_at_index(int(user_input[2]) , user_input[1])
                lista.traverse_list()
            
            elif user_input[0]=="VNE" and len(user_input)==1:
                lista.get_count()
                print(f"O número de elementos são {lista.get_count()} ")
            
            elif user_input[0]=="VP" and len(user_input)==2:
                if lista.search_item==True:
                    lista.search_item(user_input[1])
                    print(f"O pais {user_input[1]} encontra-se na lista.")
                else:
                    print(f"O pais {user_input[1]} nao se encontra na lista")

            elif user_input[0]=="EPE" and len(user_input)==1:
                print(f"o pais {lista.start_node.get_item()} foi eliminado da lista")
                lista.delete_at_start()
                
            
            elif user_input[0]=="EUE" and len(user_input)==1:
                print(f"o pais {lista.get_last_node()} foi eliminado da lista")
                lista.delete_at_end()
                
            
            elif user_input[0]=="EP" and len(user_input)==2:
                if lista.search_item== True:
                    lista.delete_element_by_value(user_input[1])
                    print(f"O pais  {user_input[1]} foi iliminado da lista ")
                else:
                    print(f"O pais {user_input[1]} não se encontra na lista")
            
            else:
                print("Por favor verifique se todas as informações foram introduzidas.")
