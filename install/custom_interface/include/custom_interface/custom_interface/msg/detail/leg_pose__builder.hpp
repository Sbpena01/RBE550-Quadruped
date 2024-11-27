// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interface:msg/LegPose.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/leg_pose.hpp"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__LEG_POSE__BUILDER_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__LEG_POSE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interface/msg/detail/leg_pose__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interface
{

namespace msg
{

namespace builder
{

class Init_LegPose_leg_pose
{
public:
  explicit Init_LegPose_leg_pose(::custom_interface::msg::LegPose & msg)
  : msg_(msg)
  {}
  ::custom_interface::msg::LegPose leg_pose(::custom_interface::msg::LegPose::_leg_pose_type arg)
  {
    msg_.leg_pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::msg::LegPose msg_;
};

class Init_LegPose_is_swing
{
public:
  Init_LegPose_is_swing()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LegPose_leg_pose is_swing(::custom_interface::msg::LegPose::_is_swing_type arg)
  {
    msg_.is_swing = std::move(arg);
    return Init_LegPose_leg_pose(msg_);
  }

private:
  ::custom_interface::msg::LegPose msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::msg::LegPose>()
{
  return custom_interface::msg::builder::Init_LegPose_is_swing();
}

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__LEG_POSE__BUILDER_HPP_
