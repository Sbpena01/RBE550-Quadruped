// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interface:srv/ImuData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/srv/imu_data.hpp"


#ifndef CUSTOM_INTERFACE__SRV__DETAIL__IMU_DATA__BUILDER_HPP_
#define CUSTOM_INTERFACE__SRV__DETAIL__IMU_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interface/srv/detail/imu_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interface
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::srv::ImuData_Request>()
{
  return ::custom_interface::srv::ImuData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace custom_interface


namespace custom_interface
{

namespace srv
{

namespace builder
{

class Init_ImuData_Response_yaw
{
public:
  explicit Init_ImuData_Response_yaw(::custom_interface::srv::ImuData_Response & msg)
  : msg_(msg)
  {}
  ::custom_interface::srv::ImuData_Response yaw(::custom_interface::srv::ImuData_Response::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::srv::ImuData_Response msg_;
};

class Init_ImuData_Response_pitch
{
public:
  explicit Init_ImuData_Response_pitch(::custom_interface::srv::ImuData_Response & msg)
  : msg_(msg)
  {}
  Init_ImuData_Response_yaw pitch(::custom_interface::srv::ImuData_Response::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_ImuData_Response_yaw(msg_);
  }

private:
  ::custom_interface::srv::ImuData_Response msg_;
};

class Init_ImuData_Response_roll
{
public:
  Init_ImuData_Response_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImuData_Response_pitch roll(::custom_interface::srv::ImuData_Response::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_ImuData_Response_pitch(msg_);
  }

private:
  ::custom_interface::srv::ImuData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::srv::ImuData_Response>()
{
  return custom_interface::srv::builder::Init_ImuData_Response_roll();
}

}  // namespace custom_interface


namespace custom_interface
{

namespace srv
{

namespace builder
{

class Init_ImuData_Event_response
{
public:
  explicit Init_ImuData_Event_response(::custom_interface::srv::ImuData_Event & msg)
  : msg_(msg)
  {}
  ::custom_interface::srv::ImuData_Event response(::custom_interface::srv::ImuData_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::srv::ImuData_Event msg_;
};

class Init_ImuData_Event_request
{
public:
  explicit Init_ImuData_Event_request(::custom_interface::srv::ImuData_Event & msg)
  : msg_(msg)
  {}
  Init_ImuData_Event_response request(::custom_interface::srv::ImuData_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ImuData_Event_response(msg_);
  }

private:
  ::custom_interface::srv::ImuData_Event msg_;
};

class Init_ImuData_Event_info
{
public:
  Init_ImuData_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImuData_Event_request info(::custom_interface::srv::ImuData_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ImuData_Event_request(msg_);
  }

private:
  ::custom_interface::srv::ImuData_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::srv::ImuData_Event>()
{
  return custom_interface::srv::builder::Init_ImuData_Event_info();
}

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__SRV__DETAIL__IMU_DATA__BUILDER_HPP_
