def output(message: str, output_type: str ='print')-> bool:
    successful_output = False
    if output_type == 'print':
        print(message)
    else:
        print("You selected and output type that is not designed yet")
        raise NotImplementedError