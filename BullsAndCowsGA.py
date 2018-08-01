import sys, random, datetime
sys.setrecursionlimit(99999)

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
                        'score' : 0
                    })
                    break
        self.generation = 1
        self.goal = str(answer).zfill(5)
        print('[*] GOAL : ' + self.goal)

    def print_genes(self):
        "Print all genes of current generation"
        print(str(self.generation) + ' : ' + ', '.join([str(g['number']) + '(' + str(g['score']) + ')' for g in self.gene]))

    def check_goal(self):
        "Check if that any of the genes reached the goal"
        for g in self.gene:
            if g['score'] == 100:
                return True
        return False

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

    def choose(self, N):
        "Return top N genes with high scores"
        return sorted(self.gene, key=lambda k: k['score'], reverse=True)[:N]

    def crossbreed(self, g1, g2):
        "Crossbreed two of the chosen genes(g1, g2)"
        descendant = ''
        for i in range(5):
            if bool(random.getrandbits(1)) == True: 
                if g1[i] not in descendant:
                    descendant += g1[i]
                else: descendant += g2[i]
            else: 
                if g2[i] not in descendant:
                    descendant += g2[i]
                else: descendant += g1[i]
        return descendant

    def mutation(self, gene):
        "Mutate 1 digit of the given gene"
        descendant = ''
        while True:
            shift = str(random.randint(0, 9))
            if shift not in gene:
                shift_idx = random.randint(0, 4)
                for i in range(5):
                    if i == shift_idx:
                        descendant += shift
                    else: descendant += gene[i]
                break 
        return descendant

    def next(self):
        for g in self.gene:
            g['score'] = self.score(g['number'])
        # self.print_genes()
        if self.check_goal() == True:
            print('[*] Reached ' + str(self.goal) + ' in ' + str(self.generation) + ' generations')
            return self.generation
        next_gene = self.choose(4)
        for i in range(6): # Selection Pressure : 0.6
            while True:
                g = [g['number'] for g in random.sample(next_gene, 2)]
                descendant = self.crossbreed(g[0], g[1])
                if random.randint(0, 100) <= 10: # mutate with probability of 10%
                    descendant = self.mutation(descendant)
                if descendant not in [g['number'] for g in next_gene]:
                    next_gene.append({
                        'number' : descendant,
                        'score' : self.score(descendant)
                    })
                    break
        self.gene = next_gene
        self.generation += 1
        return self.next()

if __name__ == '__main__':
    # genetic = GA(input('input : '))
    # genetic = GA('12345') # for testing :)
    TEST_NUM = 10000
    s = 0
    for i in range(1, TEST_NUM + 1):
        print('[+] %dth Repeat'%i)
        genetic = GA('12345')
        s += genetic.next()
        del(genetic)
    print('\n[+] RESULT : ' + str(s/TEST_NUM)) # average of generations needed to reach goal
    with open('result.txt', 'a') as f:
        f.write(datetime.datetime.today().isoformat() + ' ' + str(s/TEST_NUM) + '\n')
