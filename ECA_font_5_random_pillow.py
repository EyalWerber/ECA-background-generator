import random


def binasci_converter(rule):

    return f'{rule:08b}'.replace('0', ' ').replace('1', '▓')


# runs algorithm randomly through a bank of good chosen rules
def rule_randomizer_bank(rule, j, change_every):
    if j % change_every == 0:
        rule = random.choice([3, 5, 11, 18, 26, 22, 30, 57, 62, 73, 106, 110,
                             126, 106, 255, 184, 178, 232, 150, 105, 104, 90, 108, 122, 1, 99, 86])
        bin_rule = binasci_converter(rule)
        with open('rules.txt', 'a') as f:
            f.writelines(f'rule: {rule}\n')
            
        return bin_rule, rule
    else:
        return binasci_converter(rule), rule


def zerolistmaker(n):
    listofzeros = ['.'] * n
    return listofzeros


def rules(nums, rule):
    if nums == [' ', ' ', ' ']:
        return rule[7]
    elif nums == [' ', ' ', '▓']:
        return rule[6]
    elif nums == [' ', '▓', ' ']:
        return rule[5]
    elif nums == [' ', '▓', '▓']:
        return rule[4]
    elif nums == ['▓', ' ', ' ']:
        return rule[3]
    elif nums == ['▓', ' ', '▓']:
        return rule[2]
    elif nums == ['▓', '▓', ' ']:
        return rule[1]
    elif nums == ['▓', '▓', '▓']:
        return rule[0]


def singular_start(dots):
    return [' ' if not i == dots/2 else '▓' for i in range(dots)]


def random_start(dots):
    return [random.choice(' ▓') for i in range(dots)]


def main(rule):

    with open('rules.txt', 'w') as f:
        pass

    whole_prompt = []
    DOTS = 2020

    # #  One starting point!
    gen_now = singular_start(DOTS)

    # Random multiple starting points
    # gen_now=random_start(DOTS)

    bin_rule = binasci_converter(rule)  # format to 8-bit binary

    gen_next = zerolistmaker(len(gen_now))
    iterations = 3001

    for j in range(iterations):

        gen_prev, gen_now = gen_now, gen_next

        for i in range(0, len(gen_now)):

            if i == 0:
                gen_next[i] = rules([' ', gen_prev[0], gen_prev[1]], bin_rule)
            elif i == len(gen_now)-1:
                gen_next[i] = rules(
                    [gen_prev[i-1], gen_prev[i], ' '], bin_rule)

            else:
                rule_view = gen_prev[i-1:i+2]
                gen_next[i] = rules(gen_prev[i-1:i+2], bin_rule)

        bin_rule, rule = rule_randomizer_bank(rule, j, 200)

        line = ''

        for i in range(len(gen_next)):
            line += gen_next[i]

        gen_next = zerolistmaker(len(gen_now))
        whole_prompt.append(line)
        # print('epoch: ',j)

    return whole_prompt