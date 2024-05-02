import XCTest
@testable import LinearSearchList

final class LinearSearchListTest: XCTestCase {
    var list: Array<Int> = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];
    
    func testLinearSearchTrueValues() {
        XCTAssertEqual(linearSearch(list, 69), true);
        XCTAssertEqual(linearSearch(list, 69420), true);
        XCTAssertEqual(linearSearch(list, 1), true);
    }
    
    func testLinearSearchFalseValues() {
        XCTAssertEqual(linearSearch(list, 1336), false);
        XCTAssertEqual(linearSearch(list, 69421), false);
        XCTAssertEqual(linearSearch(list, 0), false);
    }
}