def partition():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    global results
    results = {}
    for a in numbers:
        for b in numbers:
            if (a + b) == 10:
                results[str([a, b])] = (a * b)
            for c in numbers:
                if sum([a, b, c]) == 10:
                    results[str([a, b, c])] = (a * b * c)
                for d in numbers:
                    if sum([a, b, c, d]) == 10:
                        results[str([a, b, c, d])] = (a * b * c * d)
                    for e in numbers:
                        if sum([a, b, c, d, e]) == 10:
                            results[str([a, b, c, d, e])] = (a * b * c * d * e)
                        for f in numbers:
                            if sum([a, b, c, d, e, f]) == 10:
                                results[str([a, b, c, d, e, f])] = (a * b * c * d * e * f)


def main():
    partition()
    print(max(results, key=results.get))


if __name__ == '__main__':
    main()
