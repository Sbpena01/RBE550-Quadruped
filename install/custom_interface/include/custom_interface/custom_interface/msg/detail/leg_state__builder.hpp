// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interface:msg/LegState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/leg_state.hpp"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__BUILDER_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interface/msg/detail/leg_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interface
{

namespace msg
{

namespace builder
{

class Init_LegState_pose
{
public:
  explicit Init_LegState_pose(::custom_interface::msg::LegState & msg)
  : msg_(msg)
  {}
  ::custom_interface::msg::LegState pose(::custom_interface::msg::LegState::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::msg::LegState msg_;
};

class Init_LegState_is_swing
{
public:
  explicit Init_LegState_is_swing(::custom_interface::msg::LegState & msg)
  : msg_(msg)
  {}
  Init_LegState_pose is_swing(::custom_interface::msg::LegState::_is_swing_type arg)
  {
    msg_.is_swing = std::move(arg);
    return Init_LegState_pose(msg_);
  }

private:
  ::custom_interface::msg::LegState msg_;
};

class Init_LegState_turn_right
{
public:
  explicit Init_LegState_turn_right(::custom_interface::msg::LegState & msg)
  : msg_(msg)
  {}
  Init_LegState_is_swing turn_right(::custom_interface::msg::LegState::_turn_right_type arg)
  {
    msg_.turn_right = std::move(arg);
    return Init_LegState_is_swing(msg_);
  }

private:
  ::custom_interface::msg::LegState msg_;
};

class Init_LegState_turn_left
{
public:
  explicit Init_LegState_turn_left(::custom_interface::msg::LegState & msg)
  : msg_(msg)
  {}
  Init_LegState_turn_right turn_left(::custom_interface::msg::LegState::_turn_left_type arg)
  {
    msg_.turn_left = std::move(arg);
    return Init_LegState_turn_right(msg_);
  }

private:
  ::custom_interface::msg::LegState msg_;
};

class Init_LegState_name
{
public:
  Init_LegState_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LegState_turn_left name(::custom_interface::msg::LegState::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_LegState_turn_left(msg_);
  }

private:
  ::custom_interface::msg::LegState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::msg::LegState>()
{
  return custom_interface::msg::builder::Init_LegState_name();
}

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__BUILDER_HPP_
