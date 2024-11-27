// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_interface:srv/ImuData.idl
// generated code does not contain a copyright notice
#include "custom_interface/srv/detail/imu_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
custom_interface__srv__ImuData_Request__init(custom_interface__srv__ImuData_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
custom_interface__srv__ImuData_Request__fini(custom_interface__srv__ImuData_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
custom_interface__srv__ImuData_Request__are_equal(const custom_interface__srv__ImuData_Request * lhs, const custom_interface__srv__ImuData_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
custom_interface__srv__ImuData_Request__copy(
  const custom_interface__srv__ImuData_Request * input,
  custom_interface__srv__ImuData_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

custom_interface__srv__ImuData_Request *
custom_interface__srv__ImuData_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Request * msg = (custom_interface__srv__ImuData_Request *)allocator.allocate(sizeof(custom_interface__srv__ImuData_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interface__srv__ImuData_Request));
  bool success = custom_interface__srv__ImuData_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interface__srv__ImuData_Request__destroy(custom_interface__srv__ImuData_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interface__srv__ImuData_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interface__srv__ImuData_Request__Sequence__init(custom_interface__srv__ImuData_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Request * data = NULL;

  if (size) {
    data = (custom_interface__srv__ImuData_Request *)allocator.zero_allocate(size, sizeof(custom_interface__srv__ImuData_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interface__srv__ImuData_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interface__srv__ImuData_Request__fini(&data[i - 1]);
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
custom_interface__srv__ImuData_Request__Sequence__fini(custom_interface__srv__ImuData_Request__Sequence * array)
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
      custom_interface__srv__ImuData_Request__fini(&array->data[i]);
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

custom_interface__srv__ImuData_Request__Sequence *
custom_interface__srv__ImuData_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Request__Sequence * array = (custom_interface__srv__ImuData_Request__Sequence *)allocator.allocate(sizeof(custom_interface__srv__ImuData_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interface__srv__ImuData_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interface__srv__ImuData_Request__Sequence__destroy(custom_interface__srv__ImuData_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interface__srv__ImuData_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interface__srv__ImuData_Request__Sequence__are_equal(const custom_interface__srv__ImuData_Request__Sequence * lhs, const custom_interface__srv__ImuData_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interface__srv__ImuData_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interface__srv__ImuData_Request__Sequence__copy(
  const custom_interface__srv__ImuData_Request__Sequence * input,
  custom_interface__srv__ImuData_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interface__srv__ImuData_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interface__srv__ImuData_Request * data =
      (custom_interface__srv__ImuData_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interface__srv__ImuData_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interface__srv__ImuData_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interface__srv__ImuData_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
custom_interface__srv__ImuData_Response__init(custom_interface__srv__ImuData_Response * msg)
{
  if (!msg) {
    return false;
  }
  // roll
  // pitch
  // yaw
  return true;
}

void
custom_interface__srv__ImuData_Response__fini(custom_interface__srv__ImuData_Response * msg)
{
  if (!msg) {
    return;
  }
  // roll
  // pitch
  // yaw
}

bool
custom_interface__srv__ImuData_Response__are_equal(const custom_interface__srv__ImuData_Response * lhs, const custom_interface__srv__ImuData_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // roll
  if (lhs->roll != rhs->roll) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  return true;
}

bool
custom_interface__srv__ImuData_Response__copy(
  const custom_interface__srv__ImuData_Response * input,
  custom_interface__srv__ImuData_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // roll
  output->roll = input->roll;
  // pitch
  output->pitch = input->pitch;
  // yaw
  output->yaw = input->yaw;
  return true;
}

custom_interface__srv__ImuData_Response *
custom_interface__srv__ImuData_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Response * msg = (custom_interface__srv__ImuData_Response *)allocator.allocate(sizeof(custom_interface__srv__ImuData_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interface__srv__ImuData_Response));
  bool success = custom_interface__srv__ImuData_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interface__srv__ImuData_Response__destroy(custom_interface__srv__ImuData_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interface__srv__ImuData_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interface__srv__ImuData_Response__Sequence__init(custom_interface__srv__ImuData_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Response * data = NULL;

  if (size) {
    data = (custom_interface__srv__ImuData_Response *)allocator.zero_allocate(size, sizeof(custom_interface__srv__ImuData_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interface__srv__ImuData_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interface__srv__ImuData_Response__fini(&data[i - 1]);
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
custom_interface__srv__ImuData_Response__Sequence__fini(custom_interface__srv__ImuData_Response__Sequence * array)
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
      custom_interface__srv__ImuData_Response__fini(&array->data[i]);
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

custom_interface__srv__ImuData_Response__Sequence *
custom_interface__srv__ImuData_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Response__Sequence * array = (custom_interface__srv__ImuData_Response__Sequence *)allocator.allocate(sizeof(custom_interface__srv__ImuData_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interface__srv__ImuData_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interface__srv__ImuData_Response__Sequence__destroy(custom_interface__srv__ImuData_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interface__srv__ImuData_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interface__srv__ImuData_Response__Sequence__are_equal(const custom_interface__srv__ImuData_Response__Sequence * lhs, const custom_interface__srv__ImuData_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interface__srv__ImuData_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interface__srv__ImuData_Response__Sequence__copy(
  const custom_interface__srv__ImuData_Response__Sequence * input,
  custom_interface__srv__ImuData_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interface__srv__ImuData_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interface__srv__ImuData_Response * data =
      (custom_interface__srv__ImuData_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interface__srv__ImuData_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interface__srv__ImuData_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interface__srv__ImuData_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "custom_interface/srv/detail/imu_data__functions.h"

bool
custom_interface__srv__ImuData_Event__init(custom_interface__srv__ImuData_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    custom_interface__srv__ImuData_Event__fini(msg);
    return false;
  }
  // request
  if (!custom_interface__srv__ImuData_Request__Sequence__init(&msg->request, 0)) {
    custom_interface__srv__ImuData_Event__fini(msg);
    return false;
  }
  // response
  if (!custom_interface__srv__ImuData_Response__Sequence__init(&msg->response, 0)) {
    custom_interface__srv__ImuData_Event__fini(msg);
    return false;
  }
  return true;
}

void
custom_interface__srv__ImuData_Event__fini(custom_interface__srv__ImuData_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  custom_interface__srv__ImuData_Request__Sequence__fini(&msg->request);
  // response
  custom_interface__srv__ImuData_Response__Sequence__fini(&msg->response);
}

bool
custom_interface__srv__ImuData_Event__are_equal(const custom_interface__srv__ImuData_Event * lhs, const custom_interface__srv__ImuData_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!custom_interface__srv__ImuData_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!custom_interface__srv__ImuData_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
custom_interface__srv__ImuData_Event__copy(
  const custom_interface__srv__ImuData_Event * input,
  custom_interface__srv__ImuData_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!custom_interface__srv__ImuData_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!custom_interface__srv__ImuData_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

custom_interface__srv__ImuData_Event *
custom_interface__srv__ImuData_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Event * msg = (custom_interface__srv__ImuData_Event *)allocator.allocate(sizeof(custom_interface__srv__ImuData_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interface__srv__ImuData_Event));
  bool success = custom_interface__srv__ImuData_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interface__srv__ImuData_Event__destroy(custom_interface__srv__ImuData_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interface__srv__ImuData_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interface__srv__ImuData_Event__Sequence__init(custom_interface__srv__ImuData_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Event * data = NULL;

  if (size) {
    data = (custom_interface__srv__ImuData_Event *)allocator.zero_allocate(size, sizeof(custom_interface__srv__ImuData_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interface__srv__ImuData_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interface__srv__ImuData_Event__fini(&data[i - 1]);
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
custom_interface__srv__ImuData_Event__Sequence__fini(custom_interface__srv__ImuData_Event__Sequence * array)
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
      custom_interface__srv__ImuData_Event__fini(&array->data[i]);
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

custom_interface__srv__ImuData_Event__Sequence *
custom_interface__srv__ImuData_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interface__srv__ImuData_Event__Sequence * array = (custom_interface__srv__ImuData_Event__Sequence *)allocator.allocate(sizeof(custom_interface__srv__ImuData_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interface__srv__ImuData_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interface__srv__ImuData_Event__Sequence__destroy(custom_interface__srv__ImuData_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interface__srv__ImuData_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interface__srv__ImuData_Event__Sequence__are_equal(const custom_interface__srv__ImuData_Event__Sequence * lhs, const custom_interface__srv__ImuData_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interface__srv__ImuData_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interface__srv__ImuData_Event__Sequence__copy(
  const custom_interface__srv__ImuData_Event__Sequence * input,
  custom_interface__srv__ImuData_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interface__srv__ImuData_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interface__srv__ImuData_Event * data =
      (custom_interface__srv__ImuData_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interface__srv__ImuData_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interface__srv__ImuData_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interface__srv__ImuData_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
