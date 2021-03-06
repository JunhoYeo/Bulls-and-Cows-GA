# 숫자야구 GA
Using Genetic Algorithm to solve Bulls & Cows :baseball:

## About
[Bulls & Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) are known as 'Number Baseball' in Korea. 

The rules are the same, but we also call the in-game terms differently:

- `bulls` are `strikes`
- `cows` are `balls`

Just think about baseball and you'll get the main idea. :grin:

This project uses GA to solve Bulls & Cows:

1. Generate the secret number randomly & create the first generation of genes which are scored(20pts for each strikes, 10pts for each balls).
2. Select 4 elite genes that have the most highest scores and make the next generation.
3. Crossbreed random genes until we have 6 descendant genes and add them in next generation genes(Mutations can happen with a probability of 10% while crossbreeding).
4. Switch to next generation and score the genes in the current generation.
5. Repeat step 2~4 until the exact solution(the gene with a perfect score) is found.

## Example
```
[*] GOAL : 73461
1 : 54063(40), 62158(20), 59746(30), 84097(20), 64180(30), 02639(20), 27195(20), 63479(60), 72196(40), 64520(20)
2 : 63479(60), 54063(40), 72196(40), 59746(30), 72163(60), 63499(50), 53496(50), 72496(50), 72493(50), 59726(20)
3 : 63479(60), 72163(60), 63499(50), 53496(50), 62193(30), 63179(50), 53490(40), 73196(60), 52496(30), 53196(40)
4 : 63479(60), 72163(60), 73196(60), 63499(50), 72103(40), 72196(40), 73496(70), 72106(40), 63109(40), 73106(60)
5 : 73496(70), 63479(60), 72163(60), 73196(60), 63199(40), 73166(80), 73066(70), 73169(70), 73163(80), 73063(70)
6 : 73166(80), 73163(80), 73496(70), 73066(70), 73196(60), 73896(50), 73466(90), 73169(70), 72896(30), 53466(70)
7 : 73466(90), 73166(80), 73163(80), 73496(70), 73463(90), 78163(60), 78496(50), 78462(60), 73066(70), 78162(50)
8 : 73466(90), 73463(90), 73166(80), 73163(80), 73263(70), 73266(70), 79466(70), 78163(60), 71266(60), 78263(50)
9 : 73466(90), 73463(90), 73166(80), 73163(80), 73460(80), 73160(70), 83160(50), 83460(60), 79460(60), 78160(50)
10 : 73466(90), 73463(90), 73166(80), 73163(80), 73453(70), 63453(60), 63157(50), 63451(70), 63457(60), 73457(70)
11 : 73466(90), 73463(90), 73166(80), 73163(80), 93463(70), 73469(80), 73183(60), 73489(60), 73462(80), 73486(70)
12 : 73466(90), 73463(90), 73166(80), 73163(80), 73486(70), 73169(70), 73469(80), 75186(40), 75486(50), 23486(50)
13 : 73466(90), 73463(90), 73166(80), 73163(80), 23163(60), 23466(70), 73126(60), 23166(60), 73863(70), 73266(70)
14 : 73466(90), 73463(90), 73166(80), 73163(80), 03166(60), 73462(80), 03462(60), 79166(60), 79462(60), 13462(70)
15 : 73466(90), 73463(90), 73166(80), 73163(80), 73496(70), 71466(80), 71462(70), 73462(80), 73162(70), 71563(60)
16 : 73466(90), 73463(90), 73166(80), 73163(80), 70463(70), 13463(80), 70163(60), 73406(70), 75406(50), 75463(70)
17 : 73466(90), 73463(90), 73166(80), 73163(80), 73461(100), 73161(90), 73168(70), 73108(50), 53161(70), 73468(80)
[*] Reached 73461 in 17 generations
```

## Average of generations needed to reach goal in each 10000 executions

1. When Selection Pressure is 0.5 with random goals

```
50.3837
50.1111
50.0761
```

2. When Selection Pressure is 0.6 with random goals

```
45.1001
43.9827
45.0043
```
