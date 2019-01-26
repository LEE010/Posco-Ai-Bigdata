def mean_and_var(*vectors):
    lam_mean = lambda x: sum(x)/len(x)
    mean = tuple(map(lam_mean, zip(*vectors)))
    var = map(lambda v: ((v[0]-mean[0])**2, (v[0]-mean[0])**2), vectors)
    return (mean, tuple(map(lam_mean, zip(*var))))

def main():
    v1 = (0, 1)
    v2 = (0.5, 0.5)
    v3 = (1, 0)

    m, var = mean_and_var(v1, v2, v3)
    print('평균:', m, '분산:', var)

if __name__ == '__main__':
    main()
