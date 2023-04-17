var maxArea = function (height) {
	// Use two pointers at the beginning and end of the array

	let left = 0;
	let right = height.length - 1
	let maximum = 0;

	// Loop through the array
	while (left < right) {
	  let area;

	  // Check which height is lower (left or right), and calculate the area based on the lower height
	  if (height[left] < height[right]) {
		area = height[left] * (right - left)
		// Slide the smaller of the two sides
		left++
	  } else {
		area = height[right] * (right - left)
		// Slide the smaller of the two sides
		right--
	  }

	  // Compare that to any previous value for maximum height.  If the current area exceeds the previous maximum, re-assign it to be the new maximum.
	  if (area > maximum) {
		maximum = area
	  }


	}

	return maximum


  };
