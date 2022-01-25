try:
    from stack_and_queue.queue import Queue
    from stack_and_queue.stack import Stack
    # from stack_and_queue.node import Node

except:
    from queue import Queue
    from stack import Stack
    # from node import Node


def validate_brackets(string):
    open_tags = ["{","[","("]
    closing_tags = ["}","]",")"]
    validate = []

    for i in string:
        if i in open_tags:
            validate.append(open_tags.index(i))
            print(f"this is validate open tags: {open_tags.index(i)}")


        elif i in closing_tags:
            if ((len(validate) > 0) and (closing_tags.index(i) == validate[-1])):
                print(f"this is validate closing tags: {closing_tags.index(i)}")
                validate.pop()
            else:
                return False

    if len(validate) == 0:
        return True
    else:
        return False


if __name__== "__main__":
    test1 = "[()}"
    print(test1, validate_brackets(test1))

    test2 = "[][]"
    print(test2, validate_brackets(test2))

    test3 = "([])"
    print(test3, validate_brackets(test3))

    test4 = ")))))"
    print(test4, validate_brackets(test4))

    test5 = "[[()]]"
    print(test5, validate_brackets(test5))

