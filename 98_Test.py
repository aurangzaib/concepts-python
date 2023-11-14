# ==========================================================================================================
# Problem: Missing value in each batch
# ==========================================================================================================

"""
def get_input():
    input_list = iter(range(100))
    input_batch = 10
    return input_list, input_batch


def get_batch(input_list, input_batch):
    batch_list = []
    for index, value in enumerate(input_list):
        yield value
        if index == input_batch:
            break


def handle_batch(input_list, input_batch):
    for index, _ in enumerate(input_list):
        print("Batch: ", index)
        batch_list = get_batch(input_list, input_batch)


def main():
    input_list, input_batch = get_input()
    handle_batch(input_list, input_batch)


main()
"""

# ==========================================================================================================
# Test
# ==========================================================================================================

if __name__ == "__main__":
    pass