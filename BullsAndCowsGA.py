import random

def generate_gene():
    gene = ''
    for i in range(5):
        while True:
            r = str(random.randint(0, 9))
            if r not in gene:
                gene += r
                break
    return gene

class GA:
    def __init__(self, answer):
        self.gene = []
        for i in range(10):
            while True:
                g = generate_gene()
                # first generation genes are generated randomly
                if g not in self.gene:
                    self.gene.append({
                        'number' : g,
                        'score' : 0,
                        'binary' : '{0:017b}'.format(int(g))
                    })
                    break
        self.generation = 0
        self.goal = str(answer).zfill(5)
        for g in self.gene:
            g['score'] = self.score(g['number'])
        print('[*] GOAL : ' + self.goal)

    def score(self, tries):
        "Score genes as a fitness function"
        result = { 'strike' : 0, 'ball' : 0 }
        for try_idx, try_num in enumerate(tries):
            for goal_idx, goal_num in enumerate(self.goal):
                if (try_idx == goal_idx) and (try_num == goal_num):
                    result['strike'] += 1
                elif (try_num == goal_num):
                    result['ball'] += 1
        return result['strike']*20 + result['ball']*10

if __name__ == '__main__':
    # genetic = GA(input('input : '))
    genetic = GA('12345') # for testing :)
    print(genetic.gene)
