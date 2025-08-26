weight=float(input("Enter the weight:"))
conversion = input("Enter the CONVERSION you wanna change (Kilogram(K) , Gram(G)): ")


if conversion == "K":
    num1= weight // 1000
    print(f"The conversion of {weight} gram is {num1} Kilogram ")
elif conversion =="G":
     num2 = weight * 1000
     print(f"The conversion of {weight} Kilogram is {num2} gram")
    
else:
    print("Enter a valid number")