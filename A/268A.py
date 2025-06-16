n = int(input())

home_uniforms = []
guess_uniforms = []
result = 0

for _ in range(n):
    uniforms = [int(i) for i in str(input()).split(" ")]
    home_uniforms.append(uniforms[0])
    guess_uniforms.append(uniforms[1])

for home_uniform in home_uniforms:
    result += guess_uniforms.count(home_uniform)

print(result)