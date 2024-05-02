// swift-tools-version: 5.10

import PackageDescription

let package = Package(
    name: "algorithms",
//    dependencies: [
//        .package(url: "https://github.com/realm/SwiftLint.git", from: "0.54.0")
//    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        // .executableTarget(
        //     name: "algorithms"),
        .target(
            name: "LinearSearchList"),
        .testTarget(
            name: "LinerSearchListTests",
            dependencies: ["LinearSearchList"])
    ]
)
