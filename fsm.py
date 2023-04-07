def FSMMatching(text):
    gates = {
        (0,"c"):1,
        (1,"a"):2,
        (2,"d"):3,
        (3,"a"):4,
        (4,"b"):4,      
    }
    
    gate_index = 0

    valid_index = 4

    result = None

    index_count = 0

    for word in text:
        if (gate_index,word) in gates:
            gate_index = gates[(gate_index,word)]
        else:
            gate_index = 0  
        
        if gate_index == valid_index:
            result = index_count - 2
        if word == text[index_count-1] and text[index_count-1] == "c":
            gate_index = 1       
        index_count +=1     
    if result is not None:
        print(f"cadab pattern has been found in that index: {result - 2}")
    else:
        print(f"'{text}' in this text cadab pattern does not exist")

text = "abcasgbadccadabd"
FSMMatching(text)
