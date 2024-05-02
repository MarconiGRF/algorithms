func linearSearch(_ array: Array<Int>, _ value: Int) -> Bool {
    for i: Int in (0 ..< array.count) {
        if (array[i] == value) {
            return true;
        }
    }

    return false;
}