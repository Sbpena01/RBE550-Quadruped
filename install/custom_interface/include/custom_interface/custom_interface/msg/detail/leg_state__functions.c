// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_interface:msg/LegState.idl
// generated code does not contain a copyright notice
#include "custom_interface/msg/detail/leg_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
custom_interface__msg__LegState__init(custom_interface__msg__LegState * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    custom_interface__msg__LegState__fini(msg);
    return false;
  }
  // turn_left
  // turn_right
  // is_swing
  // pose
  if (!geometry_msgs__msg__Pose__init(&msg->pose)) {
    custom_interface__msg__LegState__fini(msg);
    return false;
  }
  return true;
}

void
custom_interface__msg__LegState__fini(custom_interface__msg__LegState * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // turn_left
  // turn_right
  // is_swing
  // pose
  geometry_msgs__msg__Pose__fini(&msg->pose);
}

bool
custom_interface__msg__LegState__are_equal(const custom_interface__msg__LegState * lhs, const custom_interface__msg__LegState * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // turn_left
  if (lhs->turn_left != rhs->turn_left) {
    return false;
  }
  // turn_right
  if (lhs->turn_right != rhs->turn_right) {
    return false;
  }
  // is_swing
  if (lhs->is_swing != rhs->is_swing) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  return true;
}

bool
custom_interface__msg__LegState__copy(
  const custom_interface__msg__LegState * input,
  custom_interface__msg__LegState * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // turn_left
  output->turn_left = input->turn_left;
  // turn_right
  output->turn_right = input->turn_right;
  // is_swing
  output->is_swing = input->is_swing;
  // pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  return true;
}

custom_interface__msg__LegState *
custom_interface__msg__LegState__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__msg__LegState * msg = (custom_interface__msg__LegState *)allocator.allocate(sizeof(custom_interface__msg__LegState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interface__msg__LegState));
  bool success = custom_interface__msg__LegState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interface__msg__LegState__destroy(custom_interface__msg__LegState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interface__msg__LegState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interface__msg__LegState__Sequence__init(custom_interface__msg__LegState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__msg__LegState * data = NULL;

  if (size) {
    data = (custom_interface__msg__LegState *)allocator.zero_allocate(size, sizeof(custom_interface__msg__LegState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interface__msg__LegState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interface__msg__LegState__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_interface__msg__LegState__Sequence__fini(custom_interface__msg__LegState__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_interface__msg__LegState__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_interface__msg__LegState__Sequence *
custom_interface__msg__LegState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__msg__LegState__Sequence * array = (custom_interface__msg__LegState__Sequence *)allocator.allocate(sizeof(custom_interface__msg__LegState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interface__msg__LegState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interface__msg__LegState__Sequence__destroy(custom_interface__msg__LegState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interface__msg__LegState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interface__msg__LegState__Sequence__are_equal(const custom_interface__msg__LegState__Sequence * lhs, const custom_interface__msg__LegState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interface__msg__LegState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interface__msg__LegState__Sequence__copy(
  const custom_interface__msg__LegState__Sequence * input,
  custom_interface__msg__LegState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interface__msg__LegState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interface__msg__LegState * data =
      (custom_interface__msg__LegState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interface__msg__LegState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interface__msg__LegState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interface__msg__LegState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
