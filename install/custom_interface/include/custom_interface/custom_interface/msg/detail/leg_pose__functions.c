// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_interface:msg/LegPose.idl
// generated code does not contain a copyright notice
#include "custom_interface/msg/detail/leg_pose__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `leg_pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
custom_interface__msg__LegPose__init(custom_interface__msg__LegPose * msg)
{
  if (!msg) {
    return false;
  }
  // is_swing
  // leg_pose
  if (!geometry_msgs__msg__Pose__init(&msg->leg_pose)) {
    custom_interface__msg__LegPose__fini(msg);
    return false;
  }
  return true;
}

void
custom_interface__msg__LegPose__fini(custom_interface__msg__LegPose * msg)
{
  if (!msg) {
    return;
  }
  // is_swing
  // leg_pose
  geometry_msgs__msg__Pose__fini(&msg->leg_pose);
}

bool
custom_interface__msg__LegPose__are_equal(const custom_interface__msg__LegPose * lhs, const custom_interface__msg__LegPose * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // is_swing
  if (lhs->is_swing != rhs->is_swing) {
    return false;
  }
  // leg_pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->leg_pose), &(rhs->leg_pose)))
  {
    return false;
  }
  return true;
}

bool
custom_interface__msg__LegPose__copy(
  const custom_interface__msg__LegPose * input,
  custom_interface__msg__LegPose * output)
{
  if (!input || !output) {
    return false;
  }
  // is_swing
  output->is_swing = input->is_swing;
  // leg_pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->leg_pose), &(output->leg_pose)))
  {
    return false;
  }
  return true;
}

custom_interface__msg__LegPose *
custom_interface__msg__LegPose__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__msg__LegPose * msg = (custom_interface__msg__LegPose *)allocator.allocate(sizeof(custom_interface__msg__LegPose), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interface__msg__LegPose));
  bool success = custom_interface__msg__LegPose__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interface__msg__LegPose__destroy(custom_interface__msg__LegPose * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interface__msg__LegPose__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interface__msg__LegPose__Sequence__init(custom_interface__msg__LegPose__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__msg__LegPose * data = NULL;

  if (size) {
    data = (custom_interface__msg__LegPose *)allocator.zero_allocate(size, sizeof(custom_interface__msg__LegPose), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interface__msg__LegPose__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interface__msg__LegPose__fini(&data[i - 1]);
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
custom_interface__msg__LegPose__Sequence__fini(custom_interface__msg__LegPose__Sequence * array)
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
      custom_interface__msg__LegPose__fini(&array->data[i]);
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

custom_interface__msg__LegPose__Sequence *
custom_interface__msg__LegPose__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__msg__LegPose__Sequence * array = (custom_interface__msg__LegPose__Sequence *)allocator.allocate(sizeof(custom_interface__msg__LegPose__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interface__msg__LegPose__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interface__msg__LegPose__Sequence__destroy(custom_interface__msg__LegPose__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interface__msg__LegPose__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interface__msg__LegPose__Sequence__are_equal(const custom_interface__msg__LegPose__Sequence * lhs, const custom_interface__msg__LegPose__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interface__msg__LegPose__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interface__msg__LegPose__Sequence__copy(
  const custom_interface__msg__LegPose__Sequence * input,
  custom_interface__msg__LegPose__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interface__msg__LegPose);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interface__msg__LegPose * data =
      (custom_interface__msg__LegPose *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interface__msg__LegPose__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interface__msg__LegPose__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interface__msg__LegPose__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
