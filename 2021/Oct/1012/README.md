# 1012



| 순번 | 출처 |                          문제 번호                           |                          문제 이름                           |     다시 볼까      |
| :--: | :--: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------: |
|  01  | SWEA | <a href="https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo" target="_blank">5656</a> | <a href="https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo" target="_blank">벽돌 깨기</a> | :heavy_check_mark: |
|  02  | SWEA | <a href="https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH" target="_blank">4012</a> | <a href="https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH" target="_blank">요리사</a> | ​ |
|  03  | SWEA | <a href="https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu" target="_blank">2105</a> | <a href="https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu" target="_blank">디저트 카페</a> | :heavy_check_mark: |



### 1. 벽돌 깨기

신경써야 할 부분들이 좀 많아서 간결한 코드를 작성할 수 있는 종류의 문제는 아니었다. 그래서 사실 다시 풀긴 망설여 진다. 벽돌이 제거되는 것 자체는 평범한 DFS이나 후보는 어느 것으로 삼을지, 그 다음에 처리는 어떻게 해줄지부터...  가장 크게 헛짓(?)을 했던 것은 리스트 복사 부분이었다. 바보같게도 `lst[:][:]`와 같은 식으로 2차원 리스트가 복사될 거라 생각했고, 이 때문에 몇 시간을 날렸다. 모르는 사람이 보면 절대 모를 부분이니까... 알게 된 건, 2차원 리스트는 내가 한 방식처럼 슬라이싱을 통해서는 안 되고, `deepcopy`나 list comprehension을 병행해야 한다는 것이다. 또, 여러 글들에서 후자인 `[item[:] for item in lst]` 방식이 더 빠르다는 것 또한 보았다. 2차원 리스트를 복사해야 할 때 유의해서 꼭 사용하자. 사소한 것으로는,,, `pop`과 `insert`를 정렬하지 않고 사용해서 0을 빼고 다시 0을 넣은 것도 후회된다.



### 2. 요리사

컴비네이션을 이용해야 했다. 다른 문제라면 다시 풀겠지만 백트래킹할 부분은 적어 보여서 다시 풀진 않아도 될 것 같다.



### 3. 디저트 카페

기존의 상하좌우 탐색 대신 대각선 탐색을 해야 하는 문제였다. 중간에 경우의 수를 줄여준답시고 범위를 좁게 잡아서 처음엔 정답에 실패하였다. 이 문제, 시간이 그렇게 촉박한 문제가 아니니 실수하지 말자.

