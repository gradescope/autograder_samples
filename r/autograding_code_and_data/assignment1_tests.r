library(testthat)

# each call to test_that() produces one test
# each test represents one point value
# you can have multiple tests for each question


test_that("first (visible)", {
  
  expect_equal( sum(myVector), 6) 

})

test_that("second (invisible)", {

  expect_true(is.character(myString))
  expect_true(len(myString) > 2)

})

test_that("third", {

  expect_equal(nrow(myDataFrame), 2)
  expect_equal(myDataFrame[1,1], 700.01, tolerance=1e-3)

})
