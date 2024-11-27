// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interface:srv/ImuData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/srv/imu_data.h"


#ifndef CUSTOM_INTERFACE__SRV__DETAIL__IMU_DATA__STRUCT_H_
#define CUSTOM_INTERFACE__SRV__DETAIL__IMU_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ImuData in the package custom_interface.
typedef struct custom_interface__srv__ImuData_Request
{
  uint8_t structure_needs_at_least_one_member;
} custom_interface__srv__ImuData_Request;

// Struct for a sequence of custom_interface__srv__ImuData_Request.
typedef struct custom_interface__srv__ImuData_Request__Sequence
{
  custom_interface__srv__ImuData_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__srv__ImuData_Request__Sequence;

// Constants defined in the message

/// Struct defined in srv/ImuData in the package custom_interface.
typedef struct custom_interface__srv__ImuData_Response
{
  double roll;
  double pitch;
  double yaw;
} custom_interface__srv__ImuData_Response;

// Struct for a sequence of custom_interface__srv__ImuData_Response.
typedef struct custom_interface__srv__ImuData_Response__Sequence
{
  custom_interface__srv__ImuData_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__srv__ImuData_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  custom_interface__srv__ImuData_Event__request__MAX_SIZE = 1
};
// response
enum
{
  custom_interface__srv__ImuData_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/ImuData in the package custom_interface.
typedef struct custom_interface__srv__ImuData_Event
{
  service_msgs__msg__ServiceEventInfo info;
  custom_interface__srv__ImuData_Request__Sequence request;
  custom_interface__srv__ImuData_Response__Sequence response;
} custom_interface__srv__ImuData_Event;

// Struct for a sequence of custom_interface__srv__ImuData_Event.
typedef struct custom_interface__srv__ImuData_Event__Sequence
{
  custom_interface__srv__ImuData_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__srv__ImuData_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACE__SRV__DETAIL__IMU_DATA__STRUCT_H_
