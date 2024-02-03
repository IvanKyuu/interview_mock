from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remained_aster = []
        for aster in asteroids:
            # print(remained_aster)
            if not remained_aster:
                remained_aster.append(aster)
                continue
            back = remained_aster[-1]
            # will collide
            if aster < 0 < back:
                flag = False
                while aster < 0 < back:
                    if abs(aster) == abs(back):
                        remained_aster.pop()
                        flag = False
                        break
                    if abs(aster) > abs(back):
                        flag = True
                        remained_aster.pop()
                        if not remained_aster:
                            break
                        back = remained_aster[-1]
                    else:
                        flag = False
                        break
            # will not collide
            else:
                flag = True
            if flag:
                remained_aster.append(aster)
        return remained_aster

if __name__ == "__main__":
    s = Solution()
    print(s.asteroidCollision([10,2,-5]))
    print(s.asteroidCollision([5,10,-5]))
    print(s.asteroidCollision([8,-8]))
    print(s.asteroidCollision([-2, -2, 1, -2]))
    print(s.asteroidCollision([-2,1,1,-1]))
