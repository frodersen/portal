module.exports = {
    testEnvironment: 'jsdom',
    moduleFileExtensions: ['js', 'json', 'vue'],
    transform: {
        '^.+\\.vue$': 'vue-jest',
        '^.+\\.js$': 'babel-jest'
    },
    testMatch: [
        '**/tests/unit/**/*.spec.js'
    ],
    collectCoverage: true,
    collectCoverageFrom: [
        'src/**/*.{js,vue}',
        '!src/main.js' // No need to cover bootstrap file
    ],
    moduleNameMapper: {
        "^@/(.*)$": "<rootDir>/src/$1"
    },
    transformIgnorePatterns: [
        "/node_modules/(?!axios).+\\.js$"
    ]
};