#!/bin/bash
# Comprehensive Test Runner for Student Handout Generator
# Version: 1.0
# Usage: ./run_tests.sh [OPTIONS]
#
# Options:
#   --unit          Run only unit tests
#   --integration   Run only integration tests
#   --security      Run only security tests
#   --quick         Run quick tests only (skip slow tests)
#   --coverage      Generate coverage report only
#   --html          Open HTML coverage report after tests
#   --markers "EXPR" Run tests matching marker expression
#   --verbose       Extra verbose output
#   --help          Show this help message

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default settings
PYTEST_ARGS=""
SHOW_HTML=false
QUICK_MODE=false
TARGET_COVERAGE=80

# Function to print colored output
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Function to show help
show_help() {
    echo "Student Handout Generator - Test Runner"
    echo ""
    echo "Usage: ./run_tests.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --unit          Run only unit tests"
    echo "  --integration   Run only integration tests"
    echo "  --security      Run only security tests"
    echo "  --performance   Run only performance tests"
    echo "  --quick         Run quick tests only (skip slow tests)"
    echo "  --coverage      Generate coverage report only"
    echo "  --html          Open HTML coverage report after tests"
    echo "  --markers EXPR  Run tests matching marker expression"
    echo "  --verbose       Extra verbose output"
    echo "  --no-cov        Disable coverage reporting (faster)"
    echo "  --help          Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./run_tests.sh                     # Run all tests with coverage"
    echo "  ./run_tests.sh --unit              # Run only unit tests"
    echo "  ./run_tests.sh --quick             # Run quick tests (skip slow)"
    echo "  ./run_tests.sh --integration --html # Run integration tests, open coverage"
    echo "  ./run_tests.sh --markers \"not slow\" # Skip slow tests"
    exit 0
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --unit)
            PYTEST_ARGS="$PYTEST_ARGS -m unit"
            shift
            ;;
        --integration)
            PYTEST_ARGS="$PYTEST_ARGS -m integration"
            shift
            ;;
        --security)
            PYTEST_ARGS="$PYTEST_ARGS -m security"
            shift
            ;;
        --performance)
            PYTEST_ARGS="$PYTEST_ARGS -m performance"
            shift
            ;;
        --quick)
            QUICK_MODE=true
            PYTEST_ARGS="$PYTEST_ARGS -m 'not slow'"
            shift
            ;;
        --coverage)
            # Just run with coverage, no special markers
            shift
            ;;
        --html)
            SHOW_HTML=true
            shift
            ;;
        --markers)
            PYTEST_ARGS="$PYTEST_ARGS -m '$2'"
            shift 2
            ;;
        --verbose)
            PYTEST_ARGS="$PYTEST_ARGS -vv"
            shift
            ;;
        --no-cov)
            PYTEST_ARGS="$PYTEST_ARGS --no-cov"
            shift
            ;;
        --help)
            show_help
            ;;
        *)
            print_error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Main execution
print_header "Student Handout Generator Test Suite"

echo ""
echo "Test Configuration:"
echo "  Python version: $(python3 --version)"
echo "  Pytest version: $(python3 -m pytest --version)"
echo "  Working directory: $(pwd)"
echo "  Coverage threshold: ${TARGET_COVERAGE}%"
if [ "$QUICK_MODE" = true ]; then
    echo "  Mode: Quick (skipping slow tests)"
fi
echo ""

# Create logs directory if it doesn't exist
mkdir -p tests/logs

# Check if pytest is installed
if ! python3 -m pytest --version &> /dev/null; then
    print_error "pytest is not installed"
    echo "Install with: pip install pytest pytest-cov pytest-mock"
    exit 1
fi

# Run tests
print_header "Running Tests"
echo ""

# Execute pytest with all arguments
if python3 -m pytest tests/ $PYTEST_ARGS; then
    print_success "All tests passed!"
    TEST_STATUS=0
else
    print_error "Some tests failed"
    TEST_STATUS=1
fi

echo ""

# Check coverage if enabled (default)
if [[ ! "$PYTEST_ARGS" =~ "--no-cov" ]]; then
    print_header "Coverage Analysis"
    echo ""

    # Extract coverage percentage from pytest output or coverage report
    if command -v coverage &> /dev/null; then
        # Get total coverage
        COVERAGE_OUTPUT=$(python3 -m coverage report --precision=2 | grep TOTAL)
        COVERAGE_PERCENT=$(echo "$COVERAGE_OUTPUT" | awk '{print $4}' | sed 's/%//')

        echo "Coverage Summary:"
        echo "$COVERAGE_OUTPUT"
        echo ""

        # Check if coverage meets threshold
        if (( $(echo "$COVERAGE_PERCENT >= $TARGET_COVERAGE" | bc -l) )); then
            print_success "Coverage: ${COVERAGE_PERCENT}% (threshold: ${TARGET_COVERAGE}%)"
            COVERAGE_STATUS=0
        else
            print_error "Coverage: ${COVERAGE_PERCENT}% is below threshold of ${TARGET_COVERAGE}%"
            echo ""
            echo "Files with low coverage:"
            python3 -m coverage report --skip-covered | grep -v "100%"
            COVERAGE_STATUS=1
        fi
    else
        print_warning "Coverage tool not found, skipping coverage check"
        COVERAGE_STATUS=0
    fi

    echo ""

    # Show HTML coverage report location
    if [ -d "htmlcov" ]; then
        print_success "HTML coverage report generated: htmlcov/index.html"

        # Open HTML report if requested
        if [ "$SHOW_HTML" = true ]; then
            if command -v open &> /dev/null; then
                open htmlcov/index.html
                print_success "Opened coverage report in browser"
            elif command -v xdg-open &> /dev/null; then
                xdg-open htmlcov/index.html
                print_success "Opened coverage report in browser"
            else
                print_warning "Could not open browser automatically"
                echo "Open htmlcov/index.html manually"
            fi
        fi
    fi
else
    COVERAGE_STATUS=0
fi

# Summary
echo ""
print_header "Test Summary"
echo ""

if [ $TEST_STATUS -eq 0 ]; then
    print_success "Tests: PASSED"
else
    print_error "Tests: FAILED"
fi

if [[ ! "$PYTEST_ARGS" =~ "--no-cov" ]]; then
    if [ $COVERAGE_STATUS -eq 0 ]; then
        print_success "Coverage: PASSED"
    else
        print_error "Coverage: FAILED"
    fi
fi

echo ""

# Exit with appropriate status
if [ $TEST_STATUS -eq 0 ] && [ $COVERAGE_STATUS -eq 0 ]; then
    print_header "✓ All checks passed!"
    exit 0
else
    print_header "✗ Some checks failed"
    exit 1
fi
