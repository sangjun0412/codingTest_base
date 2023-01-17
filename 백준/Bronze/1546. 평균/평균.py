N = input()
score = list(map(int, input().split()))
maxscore = max(score)
nscore = [(i/maxscore)*100 for i in score]
print(sum(nscore)/len(nscore))