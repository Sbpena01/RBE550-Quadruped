// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interface:msg/ImuData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/imu_data.hpp"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__BUILDER_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interface/msg/detail/imu_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interface
{

namespace msg
{

namespace builder
{

class Init_ImuData_yaw
{
public:
  explicit Init_ImuData_yaw(::custom_interface::msg::ImuData & msg)
  : msg_(msg)
  {}
  ::custom_interface::msg::ImuData yaw(::custom_interface::msg::ImuData::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::msg::ImuData msg_;
};

class Init_ImuData_pitch
{
public:
  explicit Init_ImuData_pitch(::custom_interface::msg::ImuData & msg)
  : msg_(msg)
  {}
  Init_ImuData_yaw pitch(::custom_interface::msg::ImuData::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_ImuData_yaw(msg_);
  }

private:
  ::custom_interface::msg::ImuData msg_;
};

class Init_ImuData_roll
{
public:
  Init_ImuData_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImuData_pitch roll(::custom_interface::msg::ImuData::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_ImuData_pitch(msg_);
  }

private:
  ::custom_interface::msg::ImuData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::msg::ImuData>()
{
  return custom_interface::msg::builder::Init_ImuData_roll();
}

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__BUILDER_HPP_
