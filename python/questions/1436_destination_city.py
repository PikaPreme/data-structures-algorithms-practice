class Test:

    # Time Complexity O(N * 2) = O(N)
    # Space Complexity O(N)
    def destination_city( paths):
        outgoing_paths = []
        for out_flight, in_flight in paths:
            outgoing_paths.append(out_flight)
        for out_flight, in_flight in paths:
            if in_flight not in outgoing_paths:
                return in_flight


if __name__ == '__main__':
    paths = [["B", "C"], ["D","B"],["C", "A"]]
    print(Test.destination_city(paths))