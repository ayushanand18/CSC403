from math import sqrt, atan, pi

def cosine_angle(pr: list, p0: list) -> float:
    """
    Returns the angle between pr and p0 (measured as arctan in radians).
    """
    if(p0[0]>pr[0]):
        return pi/2+atan((p0[0]-pr[0])/(pr[1]-p0[1]))
    else:
        return atan((pr[1]-p0[1])/(pr[0]-p0[0]))

def ccw(p1: list, p2: list, p3: list) -> int:
    """
    Returns the cross product of the three vectors.
    """
    v1 = [p2[0]-p1[0], p2[1]-p1[1]]
    v2 = [p3[0]-p2[0], p3[1]-p2[1]]
    return v2[1]*v1[0]-v2[0]*v1[1]

def graham_scan(arr: list) -> list:
    """
    Graham Scan Algorithm to computer the convex hull of given set of points.

    :param arr: [list] The list of points in 2d plane.
    :return: [list] List of points in the convex hull.
    """
    # get the least y coordinate point
    arr.sort(key = lambda pr: pr[1])
    p0 = arr.pop(0)

    # initialize empty stack
    stack = [p0]

    # now sort according the cosine of angle with p0
    arr.sort(key = lambda pr: cosine_angle(pr, p0))
    # now delete the farthest element which has the same cosine angle
    i = 0
    while(i<arr.__len__()):
        if(i>0 and cosine_angle(arr[i-1], p0)==cosine_angle(arr[i], p0)):
            arr.pop(i-1)
        else:
            i+=1
    # push p1, and p2 into the stack
    stack.append(arr[0])
    stack.append(arr[1])
    for i in range(2, arr.__len__()):
        point = arr[i]
        # pop the last point from the stack if we turn clockwise to reach this point
        while stack.__len__()>1 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop(-1)
        stack.append(point)
    # now add p0 to complete the polygon
    stack.append(p0)
    # return the current stack at the end
    return stack
